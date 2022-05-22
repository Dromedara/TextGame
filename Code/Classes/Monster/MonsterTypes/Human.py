from Code.Classes.Monster.MonsterTypes.Monsters import Monster
import random


class Human(Monster):
    def __init__(self, lvl):
        super().__init__(lvl)
        self.protection_bonus = 1.5


class Thief(Human):

    def __init__(self, lvl):
        super().__init__(lvl)
        self.key = 'thief'
        self.lvl = random.randrange(1, 6, 1)
        self.rarity = random.randrange(1, 6, 1)
        self.attack = random.randrange(4, 7, 1) * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.defence = 2 * self.rarity * (1 + 0.1 * (self.lvl - 1)) * self.protection_bonus
        self.hp = 15 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.mana = 0 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.magic_attack = 0 * self.rarity * (1 + 0.1 * (self.lvl - 1)) + self.mana
        self.gold = self.lvl + self.rarity
        self.exp = self.lvl * self.rarity
        self.loot = []

        thief_active_skills = []
        thief_passive_skills = []

        self.active_skill = thief_active_skills
        self.passive_skill = thief_passive_skills
        
        
class Looter(Human):
    def __init__(self, lvl):
        super().__init__(lvl)
        self.key = 'looter'
        self.lvl = random.randrange(6, 11, 1)
        self.rarity = random.randrange(1, 6, 1)
        self.attack = random.randrange(3, 7, 1) * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.defence = 3 * self.rarity * (1 + 0.1 * (self.lvl - 1)) * self.protection_bonus
        self.hp = 20 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.mana = 0 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.magic_attack = 0 * self.rarity * (1 + 0.1 * (self.lvl - 1)) + self.mana
        self.gold = self.lvl + self.rarity
        self.exp = self.lvl * self.rarity
        self.loot = []

        looter_active_skills = []
        looter_passive_skills = []

        self.active_skill = looter_active_skills
        self.passive_skill = looter_passive_skills


class Mercenary(Human):
    def __init__(self, lvl):
        super().__init__(lvl)
        self.key = 'mercenary'
        self.lvl = random.randrange(11, 16, 1)
        self.rarity = random.randrange(1, 6, 1)
        self.attack = random.randrange(5, 8, 1) * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.defence = 2 * self.rarity * (1 + 0.1 * (self.lvl - 1)) * self.protection_bonus
        self.hp = 15 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.mana = 0 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.magic_attack = 0 * self.rarity * (1 + 0.1 * (self.lvl - 1)) + self.mana
        self.gold = self.lvl + self.rarity
        self.exp = self.lvl * self.rarity
        self.loot = []

        mercenary_active_skills = []
        mercenary_passive_skills = []

        self.active_skill = mercenary_active_skills
        self.passive_skill = mercenary_passive_skills


class Sorcerer(Human):
    def __init__(self, lvl):
        super().__init__(lvl)
        self.key = 'sorcerer'
        self.lvl = random.randrange(16, 21, 1)
        self.rarity = random.randrange(1, 6, 1)
        self.attack = random.randrange(1, 3, 1) * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.defence = 1 * self.rarity * (1 + 0.1 * (self.lvl - 1)) * self.protection_bonus
        self.hp = 30 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.mana = 20 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.magic_attack = random.randrange(10, 21, 1) * self.rarity * (1 + 0.1 * (self.lvl - 1)) + self.mana
        self.gold = self.lvl + self.rarity
        self.exp = self.lvl * self.rarity
        self.loot = []

        sorcerer_active_skills = []
        sorcerer_passive_skills = []  # any spell?

        self.active_skill = sorcerer_active_skills
        self.passive_skill = sorcerer_passive_skills


class Bounty_Hunter(Human):
    def __init__(self, lvl):
        super().__init__(lvl)
        self.key = 'bounty_hunter'
        self.lvl = random.randrange(21, 26, 1)
        self.rarity = random.randrange(1, 6, 1)
        self.attack = random.randrange(8, 11, 1) * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.defence = 4 * self.rarity * (1 + 0.1 * (self.lvl - 1)) * self.protection_bonus
        self.hp = 15 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.mana = 4 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.magic_attack = random.randrange(1, 3, 1) * self.rarity * (1 + 0.1 * (self.lvl - 1)) + self.mana
        self.gold = self.lvl + self.rarity
        self.exp = self.lvl * self.rarity
        self.loot = []

        bounty_hunter_active_skills = []
        bounty_hunter_passive_skills = []  # Stun?

        self.active_skill = bounty_hunter_active_skills
        self.passive_skill = bounty_hunter_passive_skills
