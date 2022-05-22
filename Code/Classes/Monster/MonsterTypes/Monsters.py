import random


class Monster:
    lvl: int
    attack: float
    defence: float
    hp: float
    mana: float
    magic_attack: float

    active_skill: []
    passive_skill: []
    loot: []

    def __init__(self, lvl):
        self.lvl = lvl
        self.attack = random.randrange(lvl * 9, lvl * 11, 1)
        self.defence = random.randrange(lvl * 9, lvl * 11, 1)
        self.hp = random.randrange(lvl * 9, lvl * 11, 1)
        self.mana = random.randrange(lvl * 9, lvl * 11, 1)
        self.magic_attack = self.mana * self.attack

        self.active_skill = []
        self.passive_skill = []
        self.loot = []