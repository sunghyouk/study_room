# 카드 게임 클래스 구현하기
# NOTE: 아직은 완전히 이해하지 못했지만 더 smart하게 바꿔야 할 가능성이 높다.

# 필요한 모듈 불러오기
from random import random


# Player class 구현하기
class Player(object):
    """플레이어"""

    def __init__(self):
        """이름을 설정하고, 손에는 아무 카드도 들고 있지 않다"""
        self.hand = []
        self.name = name

    def get_name(self):
        """플레이어 이름을 반환한다"""
        return self.name

    def add_card_to_hand(self, card):
        """card, 문자열
            플레이어 손에 정상적인 카드를 추가한다"""
        if card != None:
            self.hand.append(card)

    def remove_card_from_hand(self, card):
        """card, 문자열
            플레이어 손에서 카드를 제거한다"""
        self.hand.remove(card)

    def hand_size(self):
        """플레이어 손에 있는 카드 개수를 반환한다"""
        return len(self.hand)


# Card deck 구현하기
class CardDeck(object):
    """스페이드, 하트, 다이아몬드, 클럽의 2부터 9까지 구성된 덱"""

    def __init__(self):
        """가능한 모든 카드가 들어 있는 덱
            카드를 "2H"와 같은 문자열로 표현한다"""
        hearts = "2H, 3H, 4H, 5H, 6H, 7H, 8H, 9H"
        diamonds = "2D, 3D, 4D, 5D, 6D, 7D, 8D, 9D"
        spades = "2S, 3S, 4S, 5S, 6S, 7S, 8S, 9S"
        clubs = "2C, 3C, 4C, 5C, 6C, 7C, 8C, 9C"

        self.deck = hearts.split(',') + diamonds.split(',') + \
            spades.split(',') + clubs.split(',')

    def get_card(self):
        """임의의 카드를 하나 반환한다.
            덱에 카드가 없는 경우에는 'None'을 반환한다"""

        if len(self.deck) < 1:
            return None
        card = random.choice(self.deck)
        self.deck.remove(card)
        return card

    def compare_cards(self, card1, card2):
        """다음 규칙에 따라 더 센 카드를 반환한다.
        (1) 숫자가 더 큰 카드가 더 세다. 숫자가 같다면
        (2) 스페이드 > 하트 > 다이아몬드 > 클럽 순으로 더 세다"""

        if card1[0] > card2[0]:
            return card1
        elif card1[0] < card2[0]:
            return card2
        elif card1[1] > card2[1]:
            return card1
        else:
            return card2


# 플레이어와 카드덱 초기화하기
name1 = input("이름을 입력해 주세요. 플레이어 1: ")
player1 = Player(name1)

name2 = input("이름을 입력해 주세요. 플레이어 2: ")
player2 = Player(name2)

deck = CardDeck()

# 라운드들을 시뮬레이션

while True:
    player1_card = deck.get_card()
    player2_card = deck.get_card()
    player1.add_card_to_hand(player1_card)
    player2.add_card_to_hand(player2_card)
    if player1_card == None or player2_card == None:
        print("게임 오버. 덱에 카드가 없습니다.")
        print(name1, ": 최종 카드 수 ", player1.hand_size)
        print(name2, ": 최종 카드 수 ", player2.hand_size)
        print("승자는?")
        if player1.hand_size() > player2.hand_size():
            print(name2, " 승리!")
        elif player1.hand_size() < player2.hand_size():
            print(name1, " 승리!")
        else:
            print("비겼습니다!")
        break
    else:
        print(name1, ": ", player1_card)
        print(name2, ": ", player2_card)
        if deck.compare_cards(player1_card, player2_card) == player1_card:
            player1.remove_card_from_hand(player1_card)
            player2.add_card_to_hand(player1_card)
        else:
            player2.remove_card_from_hand(player2_card)
            player1.add_card_to_hand(player2_card)
