# -*- coding: utf-8 -*-
import numpy as np


class MulLayer:
    def __init__(self):
        self.x = None
        self.y = None

    def forward(self, x, y):
        '''순전파'''

        self.x = x
        self.y = y
        out = x * y

        return out

    def backward(self, dout):
        '''역전파'''

        dx = dout * self.y  # x와 y를 바꾼다.
        dy = dout * self.x

        return dx, dy


class AddLayer:
    def __init__(self) -> None:
        pass

    def forward(self, x, y):
        '''순전파'''

        out = x + y
        return out

    def backward(self, dout):
        '''역전파'''

        dx = dout * 1
        dy = dout * 1
        return dx, dy


class Affine:
    def __init__(self, W, b):
        self.W = W
        self.b = b
        self.x = None
        self.dW = None
        self.db = None

    def forward(self, x):
        self.x = x
        out = np.dot(x, self.W) + self.b

        return out

    def backward(self, dout):
        dx = np.dot(dout, self.W.T)
        self.dW = np.dot(self.x.T, dout)
        self.db = np.sum(dout, axis=0)

        return dx
