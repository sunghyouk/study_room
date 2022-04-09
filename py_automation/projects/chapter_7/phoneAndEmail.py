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

# TODO: 메일 주소를 위한 정규 표현식

# TODO: 클립 보드의 텍스트에서 패턴이 일치하는 것 찾기

# TODO: 결과를 클립보드에 복사하기
