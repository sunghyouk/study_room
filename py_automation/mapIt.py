#! python3
# mapIt.py 명령행이나 클립보드에 있는 주소를 활용하여 브라우저에서 지도를 실행

import sys
import webbrowser

import pyperclip

if len(sys.argv) > 1:
    # 명령행에서 주소를 받음
    address = ' '.join(sys.argv[1:])
else:
    # 클립보드에서 주소를 받음
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
