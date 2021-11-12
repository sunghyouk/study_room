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
