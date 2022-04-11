#! python3
# phoneAndEmail.py - 클립보드에서 전화번호와 이메일 찾기

import re

import pyperclip

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
    [a-zA-Z0-9.-] # 도메인 이름
    (\.[a-zA-Z]{2,4}) # .com, .net, .org 등 최상위 도메인
)''', re.VERBOSE)

# TODO: 클립 보드의 텍스트에서 패턴이 일치하는 것 찾기

# TODO: 결과를 클립보드에 복사하기
