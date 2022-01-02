# coding: utf-8
# 1.4.4 Trainer 클래스
# 1.4.3 학습용 코드 (train_custom_loop.py)와 같은 결과
import sys

from common.optimizer import SGD
from common.trainer import Trainer
from dataset import spiral

from two_layer_net import TwoLayerNet

sys.path.append('..')  # 부모 디렉터리의 파일을 가져올 수 있도록 설정


# 하이퍼파라미터 설정
max_epoch = 300
batch_size = 30
hidden_size = 10
learning_rate = 1.0

x, t = spiral.load_data()
model = TwoLayerNet(input_size=2, hidden_size=hidden_size, output_size=3)
optimizer = SGD(lr=learning_rate)

trainer = Trainer(model, optimizer)
trainer.fit(x, t, max_epoch, batch_size, eval_interval=10)
trainer.plot()
