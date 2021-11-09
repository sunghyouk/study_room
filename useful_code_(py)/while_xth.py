import time

# 상태를 기반으로 반복하기
list_test = [1, 2, 1, 2]
value = 2

while value in list_test:
    list_test.remove(value)

print(list_test)

# 시간을 기반으로 반복하기
number = 0
target_tick = time.time() + 5
while time.time() < target_tick:
    number += 1

print("5초 동안 {}번 반복했습니다.".format(number))
