# 긴 문자열을 끊어서 사전의 키로 만들고 키가 얼마나 자주 나타나는지 빈도를 값으로 만들기

lyrics = "Happy birthday to you Happy birthday to you Happy birthday to you dear Frank Happy birthday to you"

counts = {}
words = lyrics.split(" ")

for w in words:
    w = w.lower()
    if w not in counts:
        counts[w] = 1
    else:
        counts[w] += 1

print(counts)
