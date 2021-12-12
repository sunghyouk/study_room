# coding: utf-8
# 활성화함수 만들기
import numpy as np


def sigmoid():
    return 1 / (1 + np.exp(-x))


# 입력과 가중치의 곱에 편향 더하기
W1 = np.random.randn(2, 4)  # 가중치: 2행 4열
b1 = np.random.randn(4)  # 편향: 1행 4열
x = np.random.randn(10, 2)  # 입력: 미니배치형태로 10행 2열

W2 = np.random.randn(4, 3)  # 은닉층에 들어온 데이터에 4개의 가중치, 3개의 출력 행렬
b2 = np.random.randn(3)  # 편향

h = np.matmul(x, W1) + b1
a = sigmoid(h)  # 활성화 함수 적용
s = np.matmul(a, W2) + b2
