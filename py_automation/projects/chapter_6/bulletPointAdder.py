#! python3
# bulletPointAdder.py - 클립보드에 있는 텍스트의 각 줄 시작 부분에
# 위키백과 글머리 기호 추가하기

import pyperclip

text = pyperclip.paste()

# 각 줄을 분리하고 별표 기호 추가하기
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

text = '\n'.join(lines)

pyperclip.copy(text)

# NOTE: 이 script로 할 수 있는 일
"""
줄의 끝부분에 있는 공백을 제거,
텍스트를 대문자 또는 소문자로 변환
즉, 다른 종류의 텍스트 조작을 자동화하여 클립보드에서 불러 들인 후
manipulation 후 클립보드로 복사해서 내보낼 수 있음
"""
