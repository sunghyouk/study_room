def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True


print('Is 415-555-4242 a phone number?')
print(isPhoneNumber('415-555-4242'))
print('Is Yeoboseyo a phone number?')
print(isPhoneNumber('Yeoboseyo'))

# TODO: 길이가 더 긴 문자열이 전화번호인지 여부를 알아야 한다면, 아래 코드 추가
