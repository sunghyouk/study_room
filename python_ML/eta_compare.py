import matplotlib.pyplot as plt

from python_ML.adaline import AdalineGD

# eta = 0.1 or 0.0001
# 에포크 횟수 대비 비용 그래프 그려 보기
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10,4))

ada1 = AdalineGD(n_iter=10, eta=0.01).fit(X, y)
