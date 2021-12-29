# iris data 불러오기

import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 이런 식으로 같은 디렉토리 내에 다른 파일에 만들어 놓은 클래스 불러오는구나!
from perceptron import Perceptron

s = os.path.join('https://archive.ics.uci.edu', 'ml',
                 'machine-learning-databases',
                 'iris', 'iris.data')

print('URL:', s)

df = pd.read_csv(s,
                 header=None,
                 encoding='utf-8')

df.tail()

# 첫 번째 특성열 = 꽃받침 길이, 세 번째 특성열 = 꽃잎 길이
# setosa와 vesicolor를 선택
y = df.iloc[0:100, 4].values
y = np.where(y == 'Iris-setosa', -1, 1)

# 꽃받침 길이와 꽃잎 길이를 추출
X = df.iloc[0:100, [0, 2]].values

# 산점도
plt.scatter(X[:50, 0], X[:50, 1],
            color='red', marker='o', label='setosa')
plt.scatter(X[50:100, 0], X[50:100, 1],
            color='blue', marker='x', label='vesicolor')
plt.xlabel('sepal length [cm]')
plt.ylabel('petal length [cm]')
plt.legend(loc='upper left')
plt.show()

# 퍼셉트론 알고리즘 훈련
# 에포크 대비 잘못 분류된 오차를 그래프로
ppn = Perceptron(eta=0.01, n_iter=10)
ppn.fit(X, y)
plt.plot(range(1, len(ppn.errors_)+1),
         ppn.errors_, marker='o')
plt.xlabel('Epochs')
plt.ylabel('Number of updates')
plt.show()
