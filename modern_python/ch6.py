minutes_to_convert = 789 # 입력부분

hours_decimal = minutes_to_convert / 60 # 시간부분 (정수)
hours_part = int(hours_decimal)

minutes_decimal = hours_decimal - hours_part # 분 부분 (소수점 * 60의 결과값 반올림)
minutes_part = round(minutes_decimal * 60)

print(hours_part) # 출력부분
print("시간")
print(minutes_part)
print("분")

# Q6.1
# 화씨를 섭씨로 변환
fahrenheit = 75

cellcius = (fahrenheit - 32) / 1.8

print(cellcius)

# Q6.2
mile = 5

km = mile / 0.62137
m = km * 1000

print(mile)
print("마일")
print(km)
print("킬로미터")
print(m)
print("미터")
