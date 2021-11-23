# 날짜 시간과 관련된 기능을 가져오기
import datetime

# 현재 날짜와 시간 구하기
now = datetime.datetime.now()

# 출력하기
print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")

# 또 다른 방법
print("{} 년 {} 월 {} 일 {} 시 {} 분 {} 초".format(
    now.year,
    now.month,
    now.day,
    now.hour,
    now.minute,
    now.second
))

