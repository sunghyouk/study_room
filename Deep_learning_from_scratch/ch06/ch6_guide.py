# optimizer module 구현
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
optimizer_compare_naive.py: 단순 등고선 그림으로 비교
optimizer_compare_mnist.py: MNIST set으로 optimizer의 비교
'''

'''
NOTE: 가중치의 초기값 - Xavier, He 초기값과 표준 편차를 바꿔가며
weight_init_activation_histogram.py: 각 층 간 데이터 분포 히스토그램으로 확인
weight_init_compare.py: MNIST로 확인
'''

'''
NOTE: batch normalization
batch_norm_test.py'''
