from Code.Classes.Monster.MonsterTypes.Monsters import Monster
import random


class Relic(Monster):
    def __init__(self, lvl):
        super().__init__(lvl)
        self.attack_bonus = 50


class Werewolf(Relic):
    def __init__(self, lvl):
        super().__init__(lvl)
        self.key = 'werewolf'
        self.lvl = random.randrange(1, 6, 1)
        self.rarity = random.randrange(1, 6, 1)
        self.attack = random.randrange(10, 16, 1) * self.rarity * (1 + 0.1 * (self.lvl - 1)) + self.attack_bonus
        self.defence = 1 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.hp = 70 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.mana = 0 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.magic_attack = 0 * self.rarity * (1 + 0.1 * (self.lvl - 1)) + self.mana
        self.gold = self.lvl + self.rarity
        self.exp = self.lvl * self.rarity
        self.loot = [self.gold, self.exp]

        werewolf_active_skills = []
        werewolf_passive_skills = []  # bleeding?

        self.active_skill = werewolf_active_skills
        self.passive_skill = werewolf_passive_skills


class Griffin(Relic):
    def __init__(self, lvl):
        super().__init__(lvl)
        self.key = 'griffin'
        self.lvl = random.randrange(1, 6, 1)
        self.rarity = random.randrange(1, 6, 1)
        self.attack = random.randrange(12, 17, 1) * self.rarity * (1 + 0.1 * (self.lvl - 1)) + self.attack_bonus
        self.defence = 3 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.hp = 40 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.mana = 0 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.magic_attack = 0 * self.rarity * (1 + 0.1 * (self.lvl - 1)) + self.mana
        self.gold = self.lvl + self.rarity
        self.exp = self.lvl * self.rarity
        self.loot = [self.gold, self.exp]

        griffin_active_skills = []
        griffin_passive_skills = []

        self.active_skill = griffin_active_skills
        self.passive_skill = griffin_passive_skills


class Stryga(Relic):
    def __init__(self, lvl):
        super().__init__(lvl)
        self.key = 'stryga'
        self.lvl = random.randrange(1, 6, 1)
        self.rarity = random.randrange(1, 6, 1)
        self.attack = random.randrange(13, 18, 1) * self.rarity * (1 + 0.1 * (self.lvl - 1)) + self.attack_bonus
        self.defence = 2 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.hp = 25 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.mana = 0 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.magic_attack = 0 * self.rarity * (1 + 0.1 * (self.lvl - 1)) + self.mana
        self.gold = self.lvl + self.rarity
        self.exp = self.lvl * self.rarity
        self.loot = [self.gold, self.exp]

        stryga_active_skills = []
        stryga_passive_skills = []

        self.active_skill = stryga_active_skills
        self.passive_skill = stryga_passive_skills


class Archygryphon(Relic):
    def __init__(self, lvl):
        super().__init__(lvl)
        self.key = 'archygryphon'
        self.lvl = random.randrange(1, 6, 1)
        self.rarity = random.randrange(1, 6, 1)
        self.attack = random.randrange(10, 15, 1) * self.rarity * (1 + 0.1 * (self.lvl - 1)) + self.attack_bonus
        self.defence = 2 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.hp = 45 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.mana = 0 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.magic_attack = 0 * self.rarity * (1 + 0.1 * (self.lvl - 1)) + self.mana
        self.gold = self.lvl + self.rarity
        self.exp = self.lvl * self.rarity
        self.loot = [self.gold, self.exp]

        archygryphon_active_skills = []
        archygryphon_passive_skills = []  # poison?

        self.active_skill = archygryphon_active_skills
        self.passive_skill = archygryphon_passive_skills

class Manticore(Relic):
    def __init__(self, lvl):
        super().__init__(lvl)
        self.key = 'manticore'
        self.lvl = random.randrange(1, 6, 1)
        self.rarity = random.randrange(1, 6, 1)
        self.attack = random.randrange(11, 16, 1) * self.rarity * (1 + 0.1 * (self.lvl - 1)) + self.attack_bonus
        self.defence = 3 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.hp = 50 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.mana = 0 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.magic_attack = 0 * self.rarity * (1 + 0.1 * (self.lvl - 1)) + self.mana
        self.gold = self.lvl + self.rarity
        self.exp = self.lvl * self.rarity
        self.loot = [self.gold, self.exp]

        manticore_active_skills = []
        manticore_passive_skills = []

        self.active_skill = manticore_active_skills
        self.passive_skill = manticore_passive_skills

