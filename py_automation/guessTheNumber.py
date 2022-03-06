# Chapter 2. 간단한 프로그램: 숫자 맞히기 (p55~57)

# 이것은 숫자 맞히기 게임이다.
import random

secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

# 플레이어에게 숫자를 맞힐 기회를 여섯 번 준다.
for guessTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break  # 추측이 맞았을 때

if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))
