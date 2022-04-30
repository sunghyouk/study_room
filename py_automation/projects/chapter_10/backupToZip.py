#! python3
# backupToZip.py - 전체 폴더와 내용물을
# 파일 이름_숫자 (버전이 올라갈수록 증가).zip 파일에 복사하기

import os
import zipfile


def backupToZip(folder):
    # 'folder'의 전체 내용물을 ZIP 파일에 백업

    folder = os.path.abspath(folder)  # 폴더 경로가 절대 경로인지 확인

    # 이미 존재하는 파일들을 기반 사용해야 하는 이름 정의
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number += 1

    #  zip 파일 생성
    print(f'Creating {zipFilename}...')
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # 전체 폴더 트리를 탐색하고 각 폴더에 있는 파일들을 압축하기
    for foldername, subfolders, filenames in os.walk(folder):
        print(f'Adding files in {foldername}...')
        # 현재 폴더를 zip 파일에 더하기
        backupZip.write(foldername)

        # 이 폴더에 있는 모든 파일을 zip 파일에 더하기
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue  # 이미 백업하여 생긴 zip 파일을 새 백업에 포함하지 않기
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()

    print('Done.')


backupToZip('/Users/sunghyouk/github/study_room/py_automation')
