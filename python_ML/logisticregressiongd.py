class LogisticRegressionGD(object):
    """경사 하강법을 사용한 로지스틱 회귀 분류기
    
    매개변수
    --------
    eta : float 학습률 (0.0과 1.0 사이)
    n_iter : int 훈련 데이터셋 반복 횟수
    random_state : int 가중치 무작위 초기화를 위한 난수 생성기 시드
    
    속성
    --------
    w_ : 1d_array 학습된 가중치
    cost_ : list 에포크마다 누적된 로지스틱 비용 함수 값
    
   """
    def __init__(self, eta=0.05, n_iter=100, random_state=1):
        self.eta = eta
        self.n_iter = n_iter
        self.random_state = random_state
        
    def fit(self, X, y):
        """[summary]

        Args:
            X ([type]): [description]
            y ([type]): [description]
        """
        