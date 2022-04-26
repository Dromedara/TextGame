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
        self.attack = random.randrange(lvl*9, lvl*11, 1)
        self.defence = random.randrange(lvl*9, lvl*11, 1)
        self.hp = random.randrange(lvl*9, lvl*11, 1)
        self.mana = random.randrange(lvl*9, lvl*11, 1)
        self.magic_attack = self.mana * self.attack

        self.active_skill = []
        self.passive_skill = []
        self.loot = []


class Chupakabra(Monster):

    chupakabra_active_skills = {'strait_physical_attack', 'straight_magic_attack'}
    chupakabra_passive_skills = {'healing_itself'}

    def __init__(self, lvl):
        super().__init__(lvl)
        print(self.attack)
        self.loot = ['loot1', 'loot2']
        self.active_skill.extend(self.chupakabra_active_skills)
        self.passive_skill.extend(self.chupakabra_passive_skills)
