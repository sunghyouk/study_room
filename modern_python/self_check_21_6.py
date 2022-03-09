def guessed_card(number, suit, bet):
    money_won = 0
    guessed = False
    if number == 8 and suit == "hearts":
        money_won = 10*bet
        guessed = True
    else:
        money_won = bet/10

    return (money_won, guessed)


print(guessed_card(8, "hearts", 10))
print(guessed_card("8", "hearts", 10))
guessed_card(10, "spades", 5)
(amount, did_win) = guessed_card("eight", "hearts", 80)
print(did_win)
print(amount)
