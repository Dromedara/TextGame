from Code.Classes.Monster.MonsterTypes.Monsters import Monster
import random


class Undead(Monster):
    def __init__(self, lvl):
        super().__init__(lvl)
        self.magic_attack_bonus = 30


class Skeleton(Undead):
    def __init__(self, lvl):
        super().__init__(lvl)
        self.key = 'skeleton'
        self.lvl = random.randrange(1, 6, 1)
        self.rarity = random.randrange(1, 6, 1)
        self.attack = random.randrange(2, 4, 1) * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.defence = 0 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.hp = 7 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.mana = 0 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.magic_attack = 0 * self.rarity * (1 + 0.1 * (self.lvl - 1)) + self.mana + self.magic_attack_bonus
        self.gold = self.lvl + self.rarity
        self.exp = self.lvl * self.rarity
        self.loot = []

        skeleton_active_skills = []
        skeleton_passive_skills = []
    
        self.active_skill = skeleton_active_skills
        self.passive_skill = skeleton_passive_skills


class Deadman(Undead):
    def __init__(self, lvl):
        super().__init__(lvl)
        self.key = 'deadman'
        self.lvl = random.randrange(6, 11, 1)
        self.rarity = random.randrange(1, 6, 1)
        self.attack = random.randrange(3, 6, 1) * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.defence = 2 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.hp = 13 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.mana = 0 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.magic_attack = 0 * self.rarity * (1 + 0.1 * (self.lvl - 1)) + self.mana + self.magic_attack_bonus
        self.gold = self.lvl + self.rarity
        self.exp = self.lvl * self.rarity
        self.loot = []

        deadman_active_skills = []
        deadman_passive_skills = []
    
        self.active_skill = deadman_active_skills
        self.passive_skill = deadman_passive_skills


class DeathKnight(Undead):
    def __init__(self, lvl):
        super().__init__(lvl)
        self.key = 'death_knight'
        self.lvl = random.randrange(11, 16, 1)
        self.rarity = random.randrange(1, 6, 1)
        self.attack = random.randrange(2, 7, 1) * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.defence = 5 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.hp = 18 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.mana = 0 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.magic_attack = 0 * self.rarity * (1 + 0.1 * (self.lvl - 1)) + self.mana + self.magic_attack_bonus
        self.gold = self.lvl + self.rarity
        self.exp = self.lvl * self.rarity
        self.loot = []

        death_knight_active_skills = []
        death_knight_passive_skills = []
    
        self.active_skill = death_knight_active_skills
        self.passive_skill = death_knight_passive_skills


class Lich(Undead):
    def __init__(self, lvl):
        super().__init__(lvl)
        self.key = 'lich'
        self.lvl = random.randrange(16, 21, 1)
        self.rarity = random.randrange(1, 6, 1)
        self.attack = random.randrange(2, 4, 1) * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.defence = 1 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.hp = 15 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.mana = 30 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.magic_attack = random.randrange(15, 21, 1) * self.rarity * (
                    1 + 0.1 * (self.lvl - 1)) + self.mana + self.magic_attack_bonus
        self.gold = self.lvl + self.rarity
        self.exp = self.lvl * self.rarity
        self.loot = []

        lich_active_skills = []
        lich_passive_skills = []  # any spell?
    
        self.active_skill = lich_active_skills
        self.passive_skill = lich_passive_skills
    
    
class FrostWyrm(Undead):
    def __init__(self, lvl):
        super().__init__(lvl)
        self.key = 'frost_wyrm'
        self.lvl = random.randrange(21, 26, 1)
        self.rarity = random.randrange(1, 6, 1)
        self.attack = random.randrange(15, 19, 1) * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.defence = 8 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.hp = 35 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.mana = 10 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.magic_attack = random.randrange(4, 7, 1) * self.rarity * (
                    1 + 0.1 * (self.lvl - 1)) + self.mana + self.magic_attack_bonus
        self.gold = self.lvl + self.rarity
        self.exp = self.lvl * self.rarity
        self.loot = []

        frost_wyrm_active_skills = []
        frost_wyrm_passive_skills = []  # freeze?
    
        self.active_skill = frost_wyrm_active_skills
        self.passive_skill = frost_wyrm_passive_skills
