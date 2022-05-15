from Code.Classes.Equipment.ArtefactsService.ArtefactsSubFuncs import ArtefactChecker
from Code.BasicFuncs.Game.BattelField.BattleSubFuncs import BattleChecker


class Artefact:

    id: int
    rarity: int
    cost: int
    key: str
    attack: float
    defence: float
    hp: float
    mana: float
    magic_attack: float

    active_skills: []
    passive_skills: []

    def __init__(self):
        self.id = 0
        self.rarity = 0
        self.key = ''
        self.cost = 0
        self.attack = 0
        self.defence = 0
        self.hp = 0
        self.mana = 0
        self.magic_attack = 0

        self.active_skills = []
        self.passive_skills = []

    def buy_it(self):
        pass


class SimpleSword(Artefact):

    active_simple_sword_skills = ['straight_sword_attack']

    def __init__(self, _id=0, _rarity=1, attack=0, **kwargs):
        super().__init__()
        self.id = _id
        self.rarity = _rarity
        self.key = 'simple_sword'
        self.cost = self.rarity * 5
        self.attack += ArtefactChecker.check_input_data(attack, self.rarity, self.rarity * 2)
        self.active_skills.extend(self.active_simple_sword_skills)

    @staticmethod
    def straight_sword_attack(hero, monster):
        monster.hp -= (hero.attack - 0.3 * monster.defence)
        monster.defence = BattleChecker.params_change(monster.defence, 0.3 * hero.attack)
        hero.hp -= 1
        return hero, monster


class CharmedSword(SimpleSword):

    active_charmed_sword_skills = ['forced_sword_attack', 'charmed_sword_attack']

    def __init__(self, _id=0, _rarity=1, attack=0, magic_attack=0, **kwargs):
        super().__init__()
        self.id = _id
        self.rarity = _rarity
        self.key = 'charmed_sword'
        self.cost = self.rarity * 10
        self.attack += ArtefactChecker.check_input_data(attack, self.rarity * 2, self.rarity * 4)
        self.magic_attack += ArtefactChecker.check_input_data(magic_attack, self.rarity, self.rarity * 2)
        self.active_skills.extend(self.active_charmed_sword_skills)

    @staticmethod
    def forced_sword_attack(hero, monster):
        monster.hp -= (hero.attack - 0.1 * monster.defence)
        monster.defence = BattleChecker.params_change(monster.defence, 0.5 * hero.attack)
        hero.hp -= 1.2
        return hero, monster

    @staticmethod
    def charmed_sword_attack(hero, monster):
        monster.hp -= (hero.attack - 0.2 * monster.defence)
        monster.defence = BattleChecker.params_change(monster.defence, 0.3 * hero.attack)

        if hero.mana == 0:
            hero.hp -= 2
        hero.mana = BattleChecker.params_change(hero.mana, 0.5)
        return hero, monster


class SimpleMagicAmulet(Artefact):

    passive_simple_magic_amulet = ['simple_magic_baff']

    def __init__(self, _id=0, _rarity=1, mana=0, **kwargs):
        super().__init__()
        self.id = _id
        self.rarity = _rarity
        self.key = 'simple_amulet'
        self.cost = self.rarity * 5
        self.mana += ArtefactChecker.check_input_data(mana, -(self.rarity * 3), -self.rarity)
        self.passive_skills.extend(self.passive_simple_magic_amulet)

    @staticmethod
    def simple_magic_baff(hero, monster):
        hero.hp *= 1.2
        return hero, monster


class SuperMagicAmulet(SimpleMagicAmulet):

    passive_super_magic_amulet = ['super_magic_baff']
    active_super_magic_amulet = ['super_magic_attack']

    def __init__(self, _id=0, _rarity=1, mana=0, **kwargs):
        super().__init__()
        self.id = _id
        self.rarity = _rarity
        self.key = 'super_amulet'
        self.cost = self.rarity * 10
        self.mana += ArtefactChecker.check_input_data(mana, -(self.rarity * 4), -(self.rarity * 2))
        self.passive_skills.extend(self.passive_super_magic_amulet)
        self.active_skills.extend(self.active_super_magic_amulet)

    @staticmethod
    def super_magic_baff(hero, monster):
        hero.hp *= 1.5
        return hero, monster

    @staticmethod
    def super_magic_attack(hero, monster):
        monster.hp -= (hero.magic_attack - 0.3 * monster.defence)
        monster.defence = BattleChecker.params_change(monster.defence, 0.5 * hero.magic_attack)
        return hero, monster

