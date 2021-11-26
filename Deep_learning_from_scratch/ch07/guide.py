import os
import sys

import numpy as np
from common.util import im2col

sys.path.append(os.pardir)

'''
NOTE:
Convolution의 forward, backward, Pooling의 forward, backward는 common/layers.py에 구현되어 있음
im2col, col2im 함수는 common/util.py에 구현되어 있음
'''


class Convolution:
    def __init__(self, W, b, stride=1, pad=0):
        self.W = W
        self.b = b
        self.stride = stride
        self.pad = pad

    def forward(self, x):
        FN, C, FH, FW = self.W.shape
        N, C, H, W = x.shape
        out_h = int(1 + (H + 2*self.pad - FH) / self.stride)
        out_w = int(1 + (W + 2*self.pad - FW) / self.stride)

        col = im2col(x, FH, FW, self.stride, self.pad)
        col_W = self.W.reshape(FN, -1).T
        out = np.dot(col, col_W) + self.b

        out = out.reshape(N, out_h, out_w, -1).transpose(0, 3, 1, 2)

        return out


'''
NOTE:
7.5 CNN 구현하기
simple_convnet.py에 구현
MNIST 예측하기는 train_convnet.py에 구현
'''
