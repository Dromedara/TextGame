import random


class Monster:

    lvl: int
    attack: float
    defence: float
    hp: float
    mana: float
    magic_attack: float

    attacks: []
    loot: []

    def __init__(self, lvl):
        self.lvl = lvl
        self.attack = random.randrange(lvl*9, lvl*11, 1)
        self.defence = random.randrange(lvl*9, lvl*11, 1)
        self.hp = random.randrange(lvl*9, lvl*11, 1)
        self.mana = random.randrange(lvl*9, lvl*11, 1)
        self.magic_attack = self.mana * self.attack


class Chupakabra(Monster):

    def __init__(self, lvl):
        super().__init__(lvl)

        self.loot = ['loot1', 'loot2']
        self.attacks = ['boom1', 'boom2']
