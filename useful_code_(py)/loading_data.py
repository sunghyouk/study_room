import csv

import numpy as np
import pandas as pd

# 1.
a = [[], [], [], [], [], [], []]
with open('data file.csv', 'r') as f:
    reader = csv.DictReader(f)
    i = j = 0
    for row in reader:
        a[i].append(row)
        j = j+1
        if(j % 24 == 0):
            i = i+1

x_title = ['Mon', 'Tue', 'Wed', 'Thr', 'Fri', 'Sat', 'Sun']

for i in range(0, 7):
    for j in range(0, len(a[i])):
        print(x_title[i], '[', j, '] = ', a[i][j])

# 2.
fifa2019 = pd.read_csv('fifa2019.csv')
df = pd.DataFrame.copy(fifa2019.sort_values(by='Overall', ascending=False).head(200))

# 3.
f = open('temp_ice.csv', encoding='euc-kr')
data = csv.reader(f)
header = next(data)

temp = []
ice = []

for row in data:
    temp.append(float(row[1]))
    ice.append(int(row[4]))

print(temp)
print(ice)

# 4.
data_sets = np.zeros((40, 21))

with open('csv 파일', 'w') as f:
    writer = csv.writer(f)
    for i in range(40):
        writer.writerow(data_sets[i, :])
