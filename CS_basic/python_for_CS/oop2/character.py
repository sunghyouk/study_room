# game character class
from abc import ABCMeta, abstractmethod


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
            other.get_damage(self.power, attack_kind)

    # 재정의된 메서드
    def get_damage(self, power, attack_kind):
        if attack_kind in self.skills:
            self.hp -= (power//2)
        else:
            self.hp -= power


# Charracter class를 상속하여 Monster class 만들기
class Monster(Character):
    def __init__(self, name, hp, power):
        super().__init__(name, hp, power)
        self.attack_kind = 'None'

    def attack(self, other, attack_kind):
        if self.attack_kind == attack_kind:
            other.get_damage(self.power, attack_kind)

    def get_damage(self, power, attack_kind):
        if self.attack_kind == attack_kind:
            self.hp += power
        else:
            self.hp -= power

    def get_attack_kind(self):
        return self.attack_kind


class IceMonster(Monster):
    def __init__(self, name='Ice Monster', hp=50, power=10):
        super().__init__(name, hp, power)
        self.attack_kind = 'ICE'


class FireMonster(Monster):
    def __init__(self, name='Fire Monster', hp=50, power=20):
        super().__init__(name, hp, power)
        self.attack_kind = 'FIRE'

    def fireball(self):
        print('FIREBALL!')


# 실행 부분 만들기
if __name__ == "__main__":
    player = Player('sword master', 100, 30, 'ICE')
    monsters = []
    monsters.append(IceMonster())
    monsters.append(FireMonster())

    for monster in monsters:
        print(monster)

    for monster in monsters:
        player.attack(monster, 'ICE')

    print('after the player attacked')

    for monster in monsters:
        print(monster)
    print('')

    print(player)

    for monster in monsters:
        monster.attack(player, monster.get_attack_kind())
    print('after monsters attacked')

    print(player)
