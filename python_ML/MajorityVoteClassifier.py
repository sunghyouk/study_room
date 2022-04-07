import operator

import numpy as np
from sklearn.base import BaseEstimator, ClassifierMixin, clone
from sklearn.pipeline import _name_estimators
from sklearn.preprocessing import LabelEncoder


class MajorityVoteClassifier(BaseEstimator, ClassifierMixin):
    """
    다수결 투표 앙상블 분류기

    매개변수
    ---------
    classifiers: 배열 타입, 크기 = [n_classifiers]
        앙상블에 사용할 분류기

    vote: str, {'classlabel', 'probability'}
        기본값: 'classlabel'
        'classlabel'이면 예측은 다수인 클래스 레이블의 인덱스,
        'probability'면 확률 합이 가장 큰 인덱스로 클래스 레이블을 예측 (보정된 분류기에 추천)

    weights: 배열 타입, 크기 = [n_classfiers]
        선택 사항, 기본값: None
        'int' 또는 'float' 값의 리스트가 주어지면 분류기가 이 중요도로 가중
        'weights=None이면 동일하게 취급
    """

    def __init__(self, classifiers, vote='classlabel', weights=None):

        self.classifiers = classifiers
        self.named_classifiers = {key: value for key,
                                  value in _name_estimators(classifiers)}
        self.vote = vote
        self.weights = weights

    def fit(self, X, y):
        """
        분류기를 학습합니다

        매개변수
        ---------
        X: {배열 타입, 희소행렬},
            크기 = [n_samples, n_features]
            훈련 샘플 행렬

        y: 배열 타입, 크기 = [n_samples]
            타깃 클래스 레이블 벡터

        반환값
        ---------
        self: 객체
        """

        if self.vote not in ('probability', 'classlabel'):
            raise ValueError("vote는 'probability' 또는 'classlabel'이어야 합니다."
                             "; (vote=%r)이 입력되었습니다."
                             % self.vote)

        if self.weights and len(self.weights) != len(self.classifiers):
            raise ValueError("분류기와 가중치 개수는 같아야 합니다."
                             "; 가중치 %d 개, 분류기 %d 개"
                             % (len(self.weights), len(self.classifiers)))
        # self.predict 메서드에서 np.argmax를 호출할 때
        # 클래스 레이블이 0부터 시작되어야 하므로 LabelEncoder를 사용합니다.
        self.lablenc_ = LabelEncoder()
        self.lablenc_.fit(y)
        self.classes_ = self.lablenc_.classes_
        self.classifiers_ = []
        for clf in self.classifiers:
            fitted_clf = clone(clf).fit(X, self.lablenc_.transform(y))
            self.classifiers_.append(fitted_clf)
        return self

    def predict(self, X):
        """
        X에 대한 클래스 레이블을 예측

        매개변수
        ---------
        X: {배열 타입, 희소 행렬},
            크기 = [n_samples, n_features]
            샘플 데이터 행렬

        반환값
        ---------
        maj_vote: 배열 타입, 크기 = [n_samples]
            예측된 클래스 레이블

        """
        if self.vote == "probability":
            maj_vote = np.argmax(self.predict_proba(X), axis=1)
        else:  # 'classlabel' 투표

            # clf.predict 매서드를 사용해 결과를 모음
            predictions = np.asarray([clf.predict(X) for clf in self.classifiers_]).T

            maj_vote = np.apply_along_axis(
                lambda x:
                    np.argmax(np.bincount(x,
                                          weights=self.weights)),
                    axis=1,
                    arr=predictions)
        maj_vote = self.lablenc_.inverse_transform(maj_vote)
        return maj_vote

    def predict_proba(self, X):
        """
        X에 대한 클래스 확률을 예측

        매개변수
        ---------
        X: {배열 타입, 희소 행렬},
            크기 = [n_samples, n_features]
            n_samples는 샘플의 개수, n_features는 특성의 개수인 샘플 데이터 행렬

        반환값
        ---------
        avg_proba: 배열 타입,
            크기 = [n_samples, n_classes]
            샘플마다 가중치가 적용된 클래스의 평균 확률

        """

        probas = np.asarray([clf.predict_proba(X) for clf in self.classifiers_])
        avg_proba = np.average(probas,
                               axis=0, weights=self.weights)
        return avg_proba

    def get_params(self, deep=True):
        if not deep:
            return super(MajorityVoteClassifier,
                         self).get_params(deep=False)
        else:
            out = self.named_classifiers.copy()
            for name, step in six.iteritems(self.named_classifiers):
                for key, value in six.iteritems(step.get_params(deep=True)):
                    out['%s__%s' % (name, key)] = value
            return out
