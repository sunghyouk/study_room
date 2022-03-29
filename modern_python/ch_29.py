import string


# 1. 파일을 열고 파일 내용을 읽는다.
def read_text(filename):
    """
    filename: string, 읽을 파일 이름
    returns: string, 파일의 모든 내용을 출력
    """

    inFile = open(filename, 'r')
    line = inFile.read()
    return line


text = read_text("main.tex")

# 2. 파일에 있는 모든 단어 저장하기


def find_words(text):
    """
    text: string
    returns: list. 입력 문자열인 text에 들어 있는 단어들이 들어 있다.
    """

    text = text.replace("\n", " ")
    for char in string.punctuation:
        text = text.replace(char, "")
    words = text.split(" ")

    return words


words = find_words(text)

# 3. 빈도 사전 만들기


def frequencies(words):
    """
    words: list. 단어들이 들어 있는 리스트
    returns: 입력으로 들어온 단어들의 빈도가 들어 있는 사전
    """

    freq_dict = {}
    for word in words:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1
    return freq_dict


freq_dict = frequencies(words)

# 4. 주어진 두 사전의 유사도 계산하기


def calculate_similarity(dict1, dict2):
    """
    dict1: 한 문서의 단어 빈도 사전
    dict2: 다른 문서의 단어 빈도 사전
    returns: float, 두 문서의 유사도를 표현하는 값 (1 - 같음, 0 - 완전히 다름)
    """

    diff = 0
    total = 0

    for word in dict1.keys():
        if word in dict2.keys():
            diff += abs(dict1[word] - dict2[word])
        else:
            diff += dict1[word]

    for word in dict2.keys():
        if word not in dict1.keys():
            diff += dict2[word]

    total = sum(dict1.values()) + sum(dict2.values())
    difference = diff/total
    similar = 1.0 - difference

    return round(similar, 2)
