max_tries = 21
secret_word = "lofi"
guess = input("단어를 추측해 보세요: ")
tries = 1

while secret_word != guess:
    print("지금까지 ", tries, "번 추측에 실패했습니다.")
    if max_tries == tries:
        print("추측을 모두 소비하셨습니다.")
        break
    tries += 1
    guess = input("다시 추측해 보세요: ")
if tries <= max_tries and secret_word == guess:
    print("축하합니다!")
