# Monday ~ Sunday list
a = [242, 256, 237, 223, 263, 81, 46]
print('A = ', a)

# Line graph
# 외부 모듈 불러오기 
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname='font 경로/font file').get_name()
rc('font', family=font_name)

x_data = ['Mon', 'Tue', 'Wed', 'Thr', 'Fri', 'Sat', 'Sun']

# 제목 붙이기
plt.title('일주일간 유동 인구수 데이터', fontsize=16)
plt.xlabel('요일', fontsize=12)
plt.ylabel('유동 인구수', fontsize=12)

# 꺾은 선 그리기
plt.scatter(x_data, a)
plt.plot(x_data, a)
plt.show()