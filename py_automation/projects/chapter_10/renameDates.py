#! python3
# renameDates.py - 미국식 날짜 표기 형식인 MM-DD-YYYY로 된 파일 이름을
# 유럽식 날짜 표기 형식인 DD-MM-YYYY로 변경

import os
import re
import shutil

# 미국식 날짜 표기 형식 (MM-DD-YYYY)과 매칭하는 정규 표현식 작성
datePattern = re.compile(r"""^(.*?)  # 날짜 이전의 모든 텍스트
                         ((0|1)?\d)-  # 달에 해당하는 한 자리 또는 두 자리 숫자
                         ((0|1|2|3)?\d)-  # 날에 해당하는 한 자리 또는 두 자리 숫자
                         ((19|20)\d\d)  # 연도에 해당하는 네 자리 숫자
                         (.*?)$  # 날짜 이후의 모든 텍스트
                         """, re.VERBOSE)

# 작업 디렉터리 내 모든 파일에 대해 반복하기
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

    # 날짜가 없는 파일은 건너뛰기
    if mo is None:
        continue

    # 파일 이름의 다른 부분을 가져 오기
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

# 유럽식 파일 이름 (DD-MM-YYYY) 생성
euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

# 전체 절대 경로들을 가져오기
absWorkingDir = os.path.abspath('.')
amerFilename = os.path.join(absWorkingDir, amerFilename)
euroFilename = os.path.join(absWorkingDir, euroFilename)

# 파일 이름들을 변경하기
print(f'Renaming "{amerFilename}" to "{euroFilename}"...')
shutil.move(amerFilename, euroFilename)  # 테스트 후 주석을 실행 가능하도록 바꾸기
