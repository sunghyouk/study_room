secret_number = 7
print("나는 1에서 10사이의 수를 생각하고 있어요.")
game_yn = input("게임을 하시겠나요? (y or yes로 대답해주세요)")

while game_yn == "y" or game_yn == "yes":
    guess = int(input("맞춰보세요: "))
    while guess != secret_number:
        guess = int(input("다시 맞춰보세요: "))
    print("축하합니다.")
    game_yn = input("게임을 하시겠나요? (y or yes로 대답해주세요)")
print("Bye!")
