# 함수 내에서 사전 만들기/ 밖에서 만들기 실험

# 1) 책의 코드 대로

def add_words(d, word, definition):
    """
    d, 문자열을 문자열의 리스트와 연관시키는 사전
    word, 문자열
    definition, 문자열
    d를 변경한다 즉, word:definition 쌍을 사전에 추가
    word가 이미 d에 들어 있다면 definition을 word의 값에 추가
    아무 것도 반환하지 않음
    """
    if word in d:
        d[word].append(definition)
    else:
        d[word] = [definition]


words = {}  # 빈 사전을 함수 바깥에서 정의하기
add_words(words, "box", "fight")
print(words)
