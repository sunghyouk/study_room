# optimizer module 구현
from Deep_learning_from_scratch.common.util import shuffle_dataset


class SGD:
    def __init__(self, lr=0.01):
        self.lr = lr

    def update(self, params, grads):
        for key in params.key():
            params[key] -= self.lr * grads[key]


'''
TODO: 이후 momentum, AdaGrad, Adam 방식의 optimizer에 대한 설명 및 구현이 있으나,
이는 해당 책의 github에 파일이 있어 찾아서 넣어야 함
'''

'''
NOTE: /common/optimizer.py로 class Momentum, AdaGrad, Adam 구현됨
/ch06/optimizer_compare_naive.py: 단순 등고선 그림으로 비교
/ch06/optimizer_compare_mnist.py: MNIST set으로 optimizer의 비교
'''

'''
NOTE: 가중치의 초기값 - Xavier, He 초기값과 표준 편차를 바꿔가며
/ch06/weight_init_activation_histogram.py: 각 층 간 데이터 분포 히스토그램으로 확인
/ch06/weight_init_compare.py: MNIST로 확인
'''

'''
NOTE: batch normalization
/ch06/batch_norm_test.py
'''

'''
NOTE: overfitting
MNIST에서 데이터는 줄이고 모델은 복잡하게 만들어서 overfitting 유도하기
/ch06/overfit_weight_decay.py
L2 regularization을 적용한 네트워크
/common/multi_layer_net.py
'''

'''
NOTE: dropout 적용하기
/ch06/overfit_dropout.py
구현이 아닌 source code에는 Trainer class
'''
