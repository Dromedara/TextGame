import random
from Code.BasicFuncs.Game.BattelField.BattleSubFuncs import BattleChecker


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


class Human:
    def __init__(self):
        self.protection_bonus = 1.5


class Undead:
    def __init__(self):
        self.magic_attack_bonus = 30


class Beast:
    def __init__(self):
        self.hp_bonus = 150


class Relic:
    def __init__(self):
        self.attack_bonus = 50


class Thief(Monster, Human):
    def __init__(self, lvl):
        super().__init__(lvl)
        self.key = "thief"
        self.lvl = random.randrange(1, 6, 1)
        self.rarity = random.randrange(1, 6, 1)
        self.attack = random.randrange(4, 7, 1) * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.defence = 2 * self.rarity * (1 + 0.1 * (self.lvl - 1)) * self.protection_bonus
        self.hp = 15 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.mana = 0 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.magic_attack = 0 * self.rarity * (1 + 0.1 * (self.lvl - 1)) + self.mana
        self.gold = self.lvl + self.rarity
        self.exp = self.lvl * self.rarity
        self.loot = [self.gold, self.exp]

    thief_active_skills = {'strait_physical_attack', 'straight_magic_attack'}
    thief_passive_skills = {'healing_itself'}

    @staticmethod
    def strait_physical_attack(hero, monster):
        hero.hp -= (monster.attack - 0.5 * hero.defence)
        hero.defence = BattleChecker.params_change(hero.defence, (monster.lvl % 10) + (monster.lvl / 10))
        return hero, monster

    @staticmethod
    def straight_magic_attack(hero, monster):
        hero.hp -= (monster.attack - 0.3 * hero.defence)
        hero.mana = BattleChecker.params_change(hero.mana, (monster.lvl % 10) + (monster.lvl / 10))
        return hero, monster

    @staticmethod
    def healing_itself(hero, monster):
        monster.hp += random.randrange(monster.lvl - 1, monster.lvl + 1, 1)
        return hero, monster


class Looter(Monster, Human):
    def __init__(self, lvl):
        super().__init__(lvl)
        self.key = "looter"
        self.lvl = random.randrange(6, 11, 1)
        self.rarity = random.randrange(1, 6, 1)
        self.attack = random.randrange(3, 7, 1) * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.defence = 3 * self.rarity * (1 + 0.1 * (self.lvl - 1)) * self.protection_bonus
        self.hp = 20 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.mana = 0 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.magic_attack = 0 * self.rarity * (1 + 0.1 * (self.lvl - 1)) + self.mana
        self.gold = self.lvl + self.rarity
        self.exp = self.lvl * self.rarity
        self.loot = [self.gold, self.exp]

    looter_active_skills = {'strait_physical_attack', 'straight_magic_attack'}
    looter_passive_skills = {'healing_itself'}

    @staticmethod
    def strait_physical_attack(hero, monster):
        hero.hp -= (monster.attack - 0.5 * hero.defence)
        hero.defence = BattleChecker.params_change(hero.defence, (monster.lvl % 10) + (monster.lvl / 10))
        return hero, monster

    @staticmethod
    def straight_magic_attack(hero, monster):
        hero.hp -= (monster.attack - 0.3 * hero.defence)
        hero.mana = BattleChecker.params_change(hero.mana, (monster.lvl % 10) + (monster.lvl / 10))
        return hero, monster

    @staticmethod
    def healing_itself(hero, monster):
        monster.hp += random.randrange(monster.lvl - 1, monster.lvl + 1, 1)
        return hero, monster


class Mercenary(Monster, Human):
    def __init__(self, lvl):
        super().__init__(lvl)
        self.key = "mercenary"
        self.lvl = random.randrange(11, 16, 1)
        self.rarity = random.randrange(1, 6, 1)
        self.attack = random.randrange(5, 8, 1) * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.defence = 2 * self.rarity * (1 + 0.1 * (self.lvl - 1)) * self.protection_bonus
        self.hp = 15 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.mana = 0 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.magic_attack = 0 * self.rarity * (1 + 0.1 * (self.lvl - 1)) + self.mana
        self.gold = self.lvl + self.rarity
        self.exp = self.lvl * self.rarity
        self.loot = [self.gold, self.exp]

    mercenary_active_skills = {'strait_physical_attack', 'straight_magic_attack'}
    mercenary_passive_skills = {'healing_itself'}

    @staticmethod
    def strait_physical_attack(hero, monster):
        hero.hp -= (monster.attack - 0.5 * hero.defence)
        hero.defence = BattleChecker.params_change(hero.defence, (monster.lvl % 10) + (monster.lvl / 10))
        return hero, monster

    @staticmethod
    def straight_magic_attack(hero, monster):
        hero.hp -= (monster.attack - 0.3 * hero.defence)
        hero.mana = BattleChecker.params_change(hero.mana, (monster.lvl % 10) + (monster.lvl / 10))
        return hero, monster

    @staticmethod
    def healing_itself(hero, monster):
        monster.hp += random.randrange(monster.lvl - 1, monster.lvl + 1, 1)
        return hero, monster


class Sorcerer(Monster, Human):
    def __init__(self, lvl):
        super().__init__(lvl)
        self.key = "sorcerer"
        self.lvl = random.randrange(16, 21, 1)
        self.rarity = random.randrange(1, 6, 1)
        self.attack = random.randrange(1, 3, 1) * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.defence = 1 * self.rarity * (1 + 0.1 * (self.lvl - 1)) * self.protection_bonus
        self.hp = 30 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.mana = 20 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.magic_attack = random.randrange(10, 21, 1) * self.rarity * (1 + 0.1 * (self.lvl - 1)) + self.mana
        self.gold = self.lvl + self.rarity
        self.exp = self.lvl * self.rarity
        self.loot = [self.gold, self.exp]

    sorcerer_active_skills = {'strait_physical_attack', 'straight_magic_attack'}
    sorcerer_passive_skills = {'healing_itself'}  # any spell?

    @staticmethod
    def strait_physical_attack(hero, monster):
        hero.hp -= (monster.attack - 0.5 * hero.defence)
        hero.defence = BattleChecker.params_change(hero.defence, (monster.lvl % 10) + (monster.lvl / 10))
        return hero, monster

    @staticmethod
    def straight_magic_attack(hero, monster):
        hero.hp -= (monster.attack - 0.3 * hero.defence)
        hero.mana = BattleChecker.params_change(hero.mana, (monster.lvl % 10) + (monster.lvl / 10))
        return hero, monster

    @staticmethod
    def healing_itself(hero, monster):
        monster.hp += random.randrange(monster.lvl - 1, monster.lvl + 1, 1)
        return hero, monster


class Bounty_Hunter(Monster, Human):
    def __init__(self, lvl):
        super().__init__(lvl)
        self.key = "bounty_hunter"
        self.lvl = random.randrange(21, 26, 1)
        self.rarity = random.randrange(1, 6, 1)
        self.attack = random.randrange(8, 11, 1) * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.defence = 4 * self.rarity * (1 + 0.1 * (self.lvl - 1)) * self.protection_bonus
        self.hp = 15 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.mana = 4 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.magic_attack = random.randrange(1, 3, 1) * self.rarity * (1 + 0.1 * (self.lvl - 1)) + self.mana
        self.gold = self.lvl + self.rarity
        self.exp = self.lvl * self.rarity
        self.loot = [self.gold, self.exp]

    bounty_hunter_active_skills = {'strait_physical_attack', 'straight_magic_attack'}
    bounty_hunter_passive_skills = {'healing_itself'}  # Stun?

    @staticmethod
    def strait_physical_attack(hero, monster):
        hero.hp -= (monster.attack - 0.5 * hero.defence)
        hero.defence = BattleChecker.params_change(hero.defence, (monster.lvl % 10) + (monster.lvl / 10))
        return hero, monster

    @staticmethod
    def straight_magic_attack(hero, monster):
        hero.hp -= (monster.attack - 0.3 * hero.defence)
        hero.mana = BattleChecker.params_change(hero.mana, (monster.lvl % 10) + (monster.lvl / 10))
        return hero, monster

    @staticmethod
    def healing_itself(hero, monster):
        monster.hp += random.randrange(monster.lvl - 1, monster.lvl + 1, 1)
        return hero, monster


class Skeleton(Monster, Undead):
    def __init__(self, lvl):
        super().__init__(lvl)
        self.key = "skeleton"
        self.lvl = random.randrange(1, 6, 1)
        self.rarity = random.randrange(1, 6, 1)
        self.attack = random.randrange(2, 4, 1) * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.defence = 0 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.hp = 7 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.mana = 0 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.magic_attack = 0 * self.rarity * (1 + 0.1 * (self.lvl - 1)) + self.mana + self.magic_attack_bonus
        self.gold = self.lvl + self.rarity
        self.exp = self.lvl * self.rarity
        self.loot = [self.gold, self.exp]

    skeleton_active_skills = {'strait_physical_attack', 'straight_magic_attack'}
    skeleton_passive_skills = {'healing_itself'}

    @staticmethod
    def strait_physical_attack(hero, monster):
        hero.hp -= (monster.attack - 0.5 * hero.defence)
        hero.defence = BattleChecker.params_change(hero.defence, (monster.lvl % 10) + (monster.lvl / 10))
        return hero, monster

    @staticmethod
    def straight_magic_attack(hero, monster):
        hero.hp -= (monster.attack - 0.3 * hero.defence)
        hero.mana = BattleChecker.params_change(hero.mana, (monster.lvl % 10) + (monster.lvl / 10))
        return hero, monster

    @staticmethod
    def healing_itself(hero, monster):
        monster.hp += random.randrange(monster.lvl - 1, monster.lvl + 1, 1)
        return hero, monster


class Deadman(Monster, Undead):
    def __init__(self, lvl):
        super().__init__(lvl)
        self.key = "deadman"
        self.lvl = random.randrange(6, 11, 1)
        self.rarity = random.randrange(1, 6, 1)
        self.attack = random.randrange(3, 6, 1) * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.defence = 2 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.hp = 13 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.mana = 0 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.magic_attack = 0 * self.rarity * (1 + 0.1 * (self.lvl - 1)) + self.mana + self.magic_attack_bonus
        self.gold = self.lvl + self.rarity
        self.exp = self.lvl * self.rarity
        self.loot = [self.gold, self.exp]

    deadman_active_skills = {'strait_physical_attack', 'straight_magic_attack'}
    deadman_passive_skills = {'healing_itself'}

    @staticmethod
    def strait_physical_attack(hero, monster):
        hero.hp -= (monster.attack - 0.5 * hero.defence)
        hero.defence = BattleChecker.params_change(hero.defence, (monster.lvl % 10) + (monster.lvl / 10))
        return hero, monster

    @staticmethod
    def straight_magic_attack(hero, monster):
        hero.hp -= (monster.attack - 0.3 * hero.defence)
        hero.mana = BattleChecker.params_change(hero.mana, (monster.lvl % 10) + (monster.lvl / 10))
        return hero, monster

    @staticmethod
    def healing_itself(hero, monster):
        monster.hp += random.randrange(monster.lvl - 1, monster.lvl + 1, 1)
        return hero, monster


class Death_Knight(Monster, Undead):
    def __init__(self, lvl):
        super().__init__(lvl)
        self.key = "death_knight"
        self.lvl = random.randrange(11, 16, 1)
        self.rarity = random.randrange(1, 6, 1)
        self.attack = random.randrange(2, 7, 1) * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.defence = 5 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.hp = 18 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.mana = 0 * self.rarity * (1 + 0.1 * (self.lvl - 1))
        self.magic_attack = 0 * self.rarity * (1 + 0.1 * (self.lvl - 1)) + self.mana + self.magic_attack_bonus
        self.gold = self.lvl + self.rarity
        self.exp = self.lvl * self.rarity
        self.loot = [self.gold, self.exp]

    death_knight_active_skills = {'strait_physical_attack', 'straight_magic_attack'}
    death_knight_passive_skills = {'healing_itself'}

    @staticmethod
    def strait_physical_attack(hero, monster):
        hero.hp -= (monster.attack - 0.5 * hero.defence)
        hero.defence = BattleChecker.params_change(hero.defence, (monster.lvl % 10) + (monster.lvl / 10))
        return hero, monster

    @staticmethod
    def straight_magic_attack(hero, monster):
        hero.hp -= (monster.attack - 0.3 * hero.defence)
        hero.mana = BattleChecker.params_change(hero.mana, (monster.lvl % 10) + (monster.lvl / 10))
        return hero, monster

    @staticmethod
    def healing_itself(hero, monster):
        monster.hp += random.randrange(monster.lvl - 1, monster.lvl + 1, 1)
        return hero, monster


class Lich(Monster, Undead):
    def __init__(self, lvl):
        super().__init__(lvl)
        self.key = "lich"
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
        self.loot = [self.gold, self.exp]

    lich_active_skills = {'strait_physical_attack', 'straight_magic_attack'}
    lich_passive_skills = {'healing_itself'}  # any spell?

    @staticmethod
    def strait_physical_attack(hero, monster):
        hero.hp -= (monster.attack - 0.5 * hero.defence)
        hero.defence = BattleChecker.params_change(hero.defence, (monster.lvl % 10) + (monster.lvl / 10))
        return hero, monster

    @staticmethod
    def straight_magic_attack(hero, monster):
        hero.hp -= (monster.attack - 0.3 * hero.defence)
        hero.mana = BattleChecker.params_change(hero.mana, (monster.lvl % 10) + (monster.lvl / 10))
        return hero, monster

    @staticmethod
    def healing_itself(hero, monster):
        monster.hp += random.randrange(monster.lvl - 1, monster.lvl + 1, 1)
        return hero, monster


class Frost_Wyrm(Monster, Undead):
    def __init__(self, lvl):
        super().__init__(lvl)
        self.key = "frost_wyrm"
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
        self.loot = [self.gold, self.exp]

    frost_wyrm_active_skills = {'strait_physical_attack', 'straight_magic_attack'}
    frost_wyrm_passive_skills = {'healing_itself'}  # freeze?

    @staticmethod
    def strait_physical_attack(hero, monster):
        hero.hp -= (monster.attack - 0.5 * hero.defence)
        hero.defence = BattleChecker.params_change(hero.defence, (monster.lvl % 10) + (monster.lvl / 10))
        return hero, monster

    @staticmethod
    def straight_magic_attack(hero, monster):
        hero.hp -= (monster.attack - 0.3 * hero.defence)
        hero.mana = BattleChecker.params_change(hero.mana, (monster.lvl % 10) + (monster.lvl / 10))
        return hero, monster

    @staticmethod
    def healing_itself(hero, monster):
        monster.hp += random.randrange(monster.lvl - 1, monster.lvl + 1, 1)
        return hero, monster


class Wild_Dog(Monster, Beast):
    def __init__(self, lvl):
        super().__init__(lvl)
        self.key = "wild_dog"
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

    wild_dog_active_skills = {'strait_physical_attack', 'straight_magic_attack'}
    wild_dog_passive_skills = {'healing_itself'}

    @staticmethod
    def strait_physical_attack(hero, monster):
        hero.hp -= (monster.attack - 0.5 * hero.defence)
        hero.defence = BattleChecker.params_change(hero.defence, (monster.lvl % 10) + (monster.lvl / 10))
        return hero, monster

    @staticmethod
    def straight_magic_attack(hero, monster):
        hero.hp -= (monster.attack - 0.3 * hero.defence)
        hero.mana = BattleChecker.params_change(hero.mana, (monster.lvl % 10) + (monster.lvl / 10))
        return hero, monster

    @staticmethod
    def healing_itself(hero, monster):
        monster.hp += random.randrange(monster.lvl - 1, monster.lvl + 1, 1)
        return hero, monster


class Wolf(Monster, Beast):
    def __init__(self, lvl):
        super().__init__(lvl)
        self.key = "wolf"
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

    wolf_active_skills = {'strait_physical_attack', 'straight_magic_attack'}
    wolf_passive_skills = {'healing_itself'}

    @staticmethod
    def strait_physical_attack(hero, monster):
        hero.hp -= (monster.attack - 0.5 * hero.defence)
        hero.defence = BattleChecker.params_change(hero.defence, (monster.lvl % 10) + (monster.lvl / 10))
        return hero, monster

    @staticmethod
    def straight_magic_attack(hero, monster):
        hero.hp -= (monster.attack - 0.3 * hero.defence)
        hero.mana = BattleChecker.params_change(hero.mana, (monster.lvl % 10) + (monster.lvl / 10))
        return hero, monster

    @staticmethod
    def healing_itself(hero, monster):
        monster.hp += random.randrange(monster.lvl - 1, monster.lvl + 1, 1)
        return hero, monster


class Lynx(Monster, Beast):
    def __init__(self, lvl):
        super().__init__(lvl)
        self.key = "lynx"
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

    lynx_active_skills = {'strait_physical_attack', 'straight_magic_attack'}
    lynx_passive_skills = {'healing_itself'}

    @staticmethod
    def strait_physical_attack(hero, monster):
        hero.hp -= (monster.attack - 0.5 * hero.defence)
        hero.defence = BattleChecker.params_change(hero.defence, (monster.lvl % 10) + (monster.lvl / 10))
        return hero, monster

    @staticmethod
    def straight_magic_attack(hero, monster):
        hero.hp -= (monster.attack - 0.3 * hero.defence)
        hero.mana = BattleChecker.params_change(hero.mana, (monster.lvl % 10) + (monster.lvl / 10))
        return hero, monster

    @staticmethod
    def healing_itself(hero, monster):
        monster.hp += random.randrange(monster.lvl - 1, monster.lvl + 1, 1)
        return hero, monster


class Bear(Monster, Beast):
    def __init__(self, lvl):
        super().__init__(lvl)
        self.key = "bear"
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

    bear_active_skills = {'strait_physical_attack', 'straight_magic_attack'}
    bear_passive_skills = {'healing_itself'}  # stun?

    @staticmethod
    def strait_physical_attack(hero, monster):
        hero.hp -= (monster.attack - 0.5 * hero.defence)
        hero.defence = BattleChecker.params_change(hero.defence, (monster.lvl % 10) + (monster.lvl / 10))
        return hero, monster

    @staticmethod
    def straight_magic_attack(hero, monster):
        hero.hp -= (monster.attack - 0.3 * hero.defence)
        hero.mana = BattleChecker.params_change(hero.mana, (monster.lvl % 10) + (monster.lvl / 10))
        return hero, monster

    @staticmethod
    def healing_itself(hero, monster):
        monster.hp += random.randrange(monster.lvl - 1, monster.lvl + 1, 1)
        return hero, monster


class Puma(Monster, Beast):
    def __init__(self, lvl):
        super().__init__(lvl)
        self.key = "puma"
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

    puma_active_skills = {'strait_physical_attack', 'straight_magic_attack'}
    puma_passive_skills = {'healing_itself'}  # bleeding?

    @staticmethod
    def strait_physical_attack(hero, monster):
        hero.hp -= (monster.attack - 0.5 * hero.defence)
        hero.defence = BattleChecker.params_change(hero.defence, (monster.lvl % 10) + (monster.lvl / 10))
        return hero, monster

    @staticmethod
    def straight_magic_attack(hero, monster):
        hero.hp -= (monster.attack - 0.3 * hero.defence)
        hero.mana = BattleChecker.params_change(hero.mana, (monster.lvl % 10) + (monster.lvl / 10))
        return hero, monster

    @staticmethod
    def healing_itself(hero, monster):
        monster.hp += random.randrange(monster.lvl - 1, monster.lvl + 1, 1)
        return hero, monster


class Werewolf(Monster, Relic):
    def __init__(self, lvl):
        super().__init__(lvl)
        self.key = "werewolf"
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

    werewolf_active_skills = {'strait_physical_attack', 'straight_magic_attack'}
    werewolf_passive_skills = {'healing_itself'}  # bleeding?

    @staticmethod
    def strait_physical_attack(hero, monster):
        hero.hp -= (monster.attack - 0.5 * hero.defence)
        hero.defence = BattleChecker.params_change(hero.defence, (monster.lvl % 10) + (monster.lvl / 10))
        return hero, monster

    @staticmethod
    def straight_magic_attack(hero, monster):
        hero.hp -= (monster.attack - 0.3 * hero.defence)
        hero.mana = BattleChecker.params_change(hero.mana, (monster.lvl % 10) + (monster.lvl / 10))
        return hero, monster

    @staticmethod
    def healing_itself(hero, monster):
        monster.hp += random.randrange(monster.lvl - 1, monster.lvl + 1, 1)
        return hero, monster


class Griffin(Monster, Relic):
    def __init__(self, lvl):
        super().__init__(lvl)
        self.key = "griffin"
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

    griffin_active_skills = {'strait_physical_attack', 'straight_magic_attack'}
    griffin_passive_skills = {'healing_itself'}

    @staticmethod
    def strait_physical_attack(hero, monster):
        hero.hp -= (monster.attack - 0.5 * hero.defence)
        hero.defence = BattleChecker.params_change(hero.defence, (monster.lvl % 10) + (monster.lvl / 10))
        return hero, monster

    @staticmethod
    def straight_magic_attack(hero, monster):
        hero.hp -= (monster.attack - 0.3 * hero.defence)
        hero.mana = BattleChecker.params_change(hero.mana, (monster.lvl % 10) + (monster.lvl / 10))
        return hero, monster

    @staticmethod
    def healing_itself(hero, monster):
        monster.hp += random.randrange(monster.lvl - 1, monster.lvl + 1, 1)
        return hero, monster


class Stryga(Monster, Relic):
    def __init__(self, lvl):
        super().__init__(lvl)
        self.key = "stryga"
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

    stryga_active_skills = {'strait_physical_attack', 'straight_magic_attack'}
    stryga_passive_skills = {'healing_itself'}

    @staticmethod
    def strait_physical_attack(hero, monster):
        hero.hp -= (monster.attack - 0.5 * hero.defence)
        hero.defence = BattleChecker.params_change(hero.defence, (monster.lvl % 10) + (monster.lvl / 10))
        return hero, monster

    @staticmethod
    def straight_magic_attack(hero, monster):
        hero.hp -= (monster.attack - 0.3 * hero.defence)
        hero.mana = BattleChecker.params_change(hero.mana, (monster.lvl % 10) + (monster.lvl / 10))
        return hero, monster

    @staticmethod
    def healing_itself(hero, monster):
        monster.hp += random.randrange(monster.lvl - 1, monster.lvl + 1, 1)
        return hero, monster


class Archygryphon(Monster, Relic):
    def __init__(self, lvl):
        super().__init__(lvl)
        self.key = "archygryphon"
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

    archygryphon_active_skills = {'strait_physical_attack', 'straight_magic_attack'}
    archygryphon_passive_skills = {'healing_itself'}  # poison?

    @staticmethod
    def strait_physical_attack(hero, monster):
        hero.hp -= (monster.attack - 0.5 * hero.defence)
        hero.defence = BattleChecker.params_change(hero.defence, (monster.lvl % 10) + (monster.lvl / 10))
        return hero, monster

    @staticmethod
    def straight_magic_attack(hero, monster):
        hero.hp -= (monster.attack - 0.3 * hero.defence)
        hero.mana = BattleChecker.params_change(hero.mana, (monster.lvl % 10) + (monster.lvl / 10))
        return hero, monster

    @staticmethod
    def healing_itself(hero, monster):
        monster.hp += random.randrange(monster.lvl - 1, monster.lvl + 1, 1)
        return hero, monster


class Manticore(Monster, Relic):
    def __init__(self, lvl):
        super().__init__(lvl)
        self.key = "manticore"
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

    manticore_active_skills = {'strait_physical_attack', 'straight_magic_attack'}
    manticore_passive_skills = {'healing_itself'}

    @staticmethod
    def strait_physical_attack(hero, monster):
        hero.hp -= (monster.attack - 0.5 * hero.defence)
        hero.defence = BattleChecker.params_change(hero.defence, (monster.lvl % 10) + (monster.lvl / 10))
        return hero, monster

    @staticmethod
    def straight_magic_attack(hero, monster):
        hero.hp -= (monster.attack - 0.3 * hero.defence)
        hero.mana = BattleChecker.params_change(hero.mana, (monster.lvl % 10) + (monster.lvl / 10))
        return hero, monster

    @staticmethod
    def healing_itself(hero, monster):
        monster.hp += random.randrange(monster.lvl - 1, monster.lvl + 1, 1)
        return hero, monster
