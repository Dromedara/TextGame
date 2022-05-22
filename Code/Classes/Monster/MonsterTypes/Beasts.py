from Code.Classes.Monster.MonsterTypes.Monsters import Monster
from Code.BasicFuncs.Game.BattelField.BattleSubFuncs import BattleChecker
import random


class Beast(Monster):
    def __init__(self, lvl):
        super().__init__(lvl)
        self.hp_bonus = 150


class WildDog(Beast):
    
    def __init__(self, lvl):
        super().__init__(lvl)
        self.key = 'wild_dog'
        self.lvl = random.randrange(1, 6, 1)
        self.rarity = random.randrange(1, 6, 1)
        self.attack = random.randrange(3, 6, 1) * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.defence = 0 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.hp = 10 * self.rarity * (1 + 0.1 * (self.lvl - 1)) + self.hp_bonus
        self.mana = 0 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.magic_attack = 0 * self.rarity * (1 + 0.1 * (self.lvl - 1)) + self.mana
        self.gold = self.lvl + self.rarity
        self.exp = self.lvl * self.rarity
        self.loot = [self.gold, self.exp]

        wild_dog_active_skills = ['bite_attack']
        wild_dog_passive_skills = []

        self.active_skill = wild_dog_active_skills
        self.passive_skill = wild_dog_passive_skills

    @staticmethod
    def bite_attack(hero, monster):
        hero.hp -= (monster.attack - 0.5 * hero.defence)
        hero.defence = BattleChecker.params_change(hero.defence, -((monster.lvl % 10) + (monster.lvl / 10)))
        return hero, monster


class Wolf(Beast):
    def __init__(self, lvl):
        super().__init__(lvl)
        self.key = 'wolf'
        self.lvl = random.randrange(6, 11, 1)
        self.rarity = random.randrange(1, 6, 1)
        self.attack = random.randrange(4, 7, 1) * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.defence = 0 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.hp = 12 * self.rarity * (1 + 0.1 * (self.lvl - 1)) + self.hp_bonus
        self.mana = 0 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.magic_attack = 0 * self.rarity * (1 + 0.1 * (self.lvl - 1)) + self.mana
        self.gold = self.lvl + self.rarity
        self.exp = self.lvl * self.rarity
        self.loot = [self.gold, self.exp]

        wolf_active_skills = []
        wolf_passive_skills = []

        self.active_skill = wolf_active_skills
        self.passive_skill = wolf_passive_skills


class Lynx(Beast):
    def __init__(self, lvl):
        super().__init__(lvl)
        self.key = 'lynx'
        self.lvl = random.randrange(11, 16, 1)
        self.rarity = random.randrange(1, 6, 1)
        self.attack = random.randrange(5, 7, 1) * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.defence = 0 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.hp = 15 * self.rarity * (1 + 0.1 * (self.lvl - 1)) + self.hp_bonus
        self.mana = 0 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.magic_attack = 0 * self.rarity * (1 + 0.1 * (self.lvl - 1)) + self.mana
        self.gold = self.lvl + self.rarity
        self.exp = self.lvl * self.rarity
        self.loot = [self.gold, self.exp]

        lynx_active_skills = []
        lynx_passive_skills = []

        self.active_skill = lynx_active_skills
        self.passive_skill = lynx_passive_skills


class Bear(Beast):
    def __init__(self, lvl):
        super().__init__(lvl)
        self.key = 'bear'
        self.lvl = random.randrange(16, 21, 1)
        self.rarity = random.randrange(1, 6, 1)
        self.attack = random.randrange(7, 10, 1) * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.defence = 2 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.hp = 20 * self.rarity * (1 + 0.1 * (self.lvl - 1)) + self.hp_bonus
        self.mana = 0 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.magic_attack = 0 * self.rarity * (1 + 0.1 * (self.lvl - 1)) + self.mana
        self.gold = self.lvl + self.rarity
        self.exp = self.lvl * self.rarity
        self.loot = [self.gold, self.exp]

        bear_active_skills = []
        bear_passive_skills = []  # stun?

        self.active_skill = bear_active_skills
        self.passive_skill = bear_passive_skills


class Puma(Beast):
    def __init__(self, lvl):
        super().__init__(lvl)
        self.key = 'puma'
        self.lvl = random.randrange(21, 26, 1)
        self.rarity = random.randrange(1, 6, 1)
        self.attack = random.randrange(8, 11, 1) * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.defence = 0 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.hp = 10 * self.rarity * (1 + 0.1 * (self.lvl - 1)) + self.hp_bonus
        self.mana = 0 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.magic_attack = 0 * self.rarity * (1 + 0.1 * (self.lvl - 1)) + self.mana
        self.gold = self.lvl + self.rarity
        self.exp = self.lvl * self.rarity
        self.loot = [self.gold, self.exp]

        puma_active_skills = []
        puma_passive_skills = []

        self.active_skill = puma_active_skills
        self.passive_skill = puma_passive_skills
