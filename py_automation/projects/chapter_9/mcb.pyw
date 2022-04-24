#! python3
# mcb.pyw - 텍스트를 클립보드에 저장하고 불러오기
# 사용법
# python mcb.pyw save <keyword> - 클립보드의 내용을 keyword에 저장하기
# python mcb.pyw <keyword> - Keyword를 클립보드로 불러오기
# python mcb.pyw list - 모든 keyword를 클립보드로 불러오기

import shelve
import sys

import pyperclip

mcbShelf = shelve.open('mcb')

# 클립보드 내용 저장하기
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] == pyperclip.paste()
elif len(sys.argv) == 2:
    # 키워드들을 나열하고 내용 불러오기
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
