# game character class

from abc import *


# 추상 클래스로 character 만들기
class Character(metaclass=ABCMeta):
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power

    @abstractmethod
    def attack(self, other, attack_kind):
        pass

    @abstractmethod
    def get_damage(self, power, attack_kind):
        pass

    def __str__(self):
        return '{} : {}'.format(self.name, self.hp)


# character를 추상 클래스로 만들었으면 서브 클래스로 player 클래스 만들기
class Player(Character):
    def __init__(self, name='Player', hp=100, power=10, *attack_kinds):
        super().__init__(name, hp, power)

        self.skills = []
        for attack_kind in attack_kinds:
            self.skills.append(attack_kind)

    # 재정의된 메서드
    def attack(self, other, attack_kind):
        if attack_kind in self.skills:
            other.get_damage(self.power, self.attack_kind)

    # 재정의된 메서드
    def get_damage(self, power, attack_kind):
        if attack_kind in self.skills:
            self.hp -= (power//2)
        else:
            self.hp -= power

# TODO: monster, icemonster, firemonster class
# TODO: 연산자 오버로딩
