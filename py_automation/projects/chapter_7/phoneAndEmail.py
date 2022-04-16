#! python3
# phoneAndEmail.py - 클립보드에서 전화번호와 이메일 찾기

import re

import pyperclip

# 전화 번호를 위한 정규 표현식
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))? # 지역 번호
    (\s|-|\.)? # 구분자
    (\d{3}) # 첫 세자리 숫자
    (\s|-|\.) # 구분자
    (\d{4}) # 마지막 네 자리 숫자
    (\s*(ext|x|ext.)\s*(\d{2,5}))? # 내선 번호
)''', re.VERBOSE)

# 메일 주소를 위한 정규 표현식
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+ # 사용자 이름
    @ # @ 기호
    [a-zA-Z0-9.-]+ # 도메인 이름
    (\.[a-zA-Z]{2,4}) # .com, .net, .org 등 최상위 도메인
)''', re.VERBOSE)

# 클립 보드의 텍스트에서 패턴이 일치하는 것 찾기
text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.finditer(text):
    matches.append(groups[0])

# 일치한 텍스트들을 클립보드에 전달
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard: ')
    print('\n'.join(matches))
else:
    print('No phone numbers or email address found.')
