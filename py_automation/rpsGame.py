# Chapter 2. 간단한 프로그램: 가위바위보 (p57-61)
import random
import sys

print('ROCK, PAPER, SCISSORS')

# 이 변수들은 이긴 횟수, 진 횟수, 비긴 횟수를 기록한다.

wins = 0
losses = 0
ties = 0

while True:  # 본 게임 반복문
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True:  # 플레이어가 값을 입력하는 반복문
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit()
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break
        print('Type one of r, p, s or q.')

    # 플레이어의 선택을 출력
    if playerMove == 'r':
        print('ROCK versus ...')
    elif playerMove == 'p':
        print('PAPER versus ...')
    elif playerMove == 's':
        print('SCISSORS versus ...')

    # 컴퓨터의 선택을 출력
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        coumputerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        coumputerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        coumputerMove = 's'
        print('SCISSORS')

    # 승리, 패배, 무승부 여부를 출력하고 기록
    if playerMove == coumputerMove:
        print('It is a tie!')
        ties += 1
    elif playerMove == 'r' and coumputerMove == 's':
        print('You win!')
        wins += 1
    elif playerMove == 'p' and coumputerMove == 'r':
        print('You win!')
        wins += 1
    elif playerMove == 's' and coumputerMove == 'p':
        print('You win!')
        wins += 1
    elif playerMove == 'r' and coumputerMove == 'p':
        print('You lose!')
        losses += 1
    elif playerMove == 'p' and coumputerMove == 's':
        print('You lose!')
        losses += 1
    elif playerMove == 's' and coumputerMove == 'r':
        print('You lose!')
        losses += 1
