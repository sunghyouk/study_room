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


mcbShelf.close()
