# -*- coding: utf-8 -*-
# numpy 배열도 지원하도록 변경
import numpy as np
import matplotlib.pyplot as plt


# 3.2.2 계단 함수 구현
def step_function(x):
    if x > 0:
        return 1
    else:
        return 0

# 3.2.3 계단 함수 graph


def step_function_np(x):
    return np.array(x > 0, dtype=int)


x = np.arange(-5.0, 5.0, 0.1)


y = step_function(x)

plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()

# 3.2.4 시그모이드 함수 구현하기


def sigmoid(x):
    return 1/(1 + np.exp(-x))

# 그래프 그리기


x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)

plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()

# 3.2.7 ReLU (rectified linear unit) 함수


def relu(x):
    return np.maximum(0, x)
