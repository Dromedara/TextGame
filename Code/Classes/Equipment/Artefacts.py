import random


class Artefact:

    attack: float
    defence: float
    hp: float
    mana: float
    magic_attack: float
    key: str

    active_skills: []
    passive_skills: []

    def __init__(self):
        self.id = 0
        self.rarity = 0
        self.key = ''
        self.attack = 0
        self.defence = 0
        self.hp = 0
        self.mana = 0
        self.magic_attack = 0

        self.active_skills = []
        self.passive_skills = []


class SimpleIronArmor(Artefact):

    def __init__(self, _id=0, _rarity=1):
        super().__init__()
        self.id = _id
        self.rarity = _rarity
        self.key = 'Simple Iron Armor'
        self.defence = random.randrange(self.rarity, self.rarity * 3, 1)


class CharmedIronArmor(SimpleIronArmor):

    passive_charmed_iron_armor = ['simple_passive_attack']

    def __init__(self, _id=0, _rarity=1):
        super().__init__()
        self.id = _id
        self.rarity = _rarity
        self.key = 'Charmed Iron Armor'
        self.defence = random.randrange(self.rarity * 5, self.rarity * 10, 1)
        self.mana = random.randrange(-(self.rarity * 2), -self.rarity, 1)
        self.magic_attack = random.randrange(self.rarity * 2, self.rarity * 3, 1)
        self.passive_skills.extend(self.passive_charmed_iron_armor)


class SimpleSword(Artefact):

    active_simple_sword_skills = ['straight_sword_attack']

    def __init__(self, _id=0, _rarity=1):
        super().__init__()
        self.id = _id
        self.rarity = _rarity
        self.key = 'Simple Sword'
        self.attack = random.randrange(self.rarity, self.rarity * 2, 1)
        self.active_skills.extend(self.active_simple_sword_skills)


class CharmedSword(SimpleSword):

    active_charmed_sword_skills = ['forced_sword_attack', 'charmed_sword_attack']

    def __init__(self, _id=0, _rarity=1):
        super().__init__()
        self.id = _id
        self.rarity = _rarity
        self.key = 'Charmed Sword'
        self.attack = random.randrange(self.rarity * 2, self.rarity * 4, 1)
        self.magic_attack = random.randrange(self.rarity, self.rarity * 2, 1)
        self.active_skills.extend(self.active_charmed_sword_skills)


class SimpleMagicAmulet(Artefact):

    passive_simple_magic_amulet = ['simple_magic_baff']

    def __init__(self, _id=0, _rarity=1):
        super().__init__()
        self.id = _id
        self.rarity = _rarity
        self.key = 'Simple Amulet'
        self.mana = random.randrange(-(self.rarity * 2), -self.rarity, 1)
        self.passive_skills.extend(self.passive_simple_magic_amulet)


class SuperMagicAmulet(SimpleMagicAmulet):
    passive_super_magic_amulet = ['super_magic_baff']
    active_super_magic_amulet = ['super_magic_attack']

    def __init__(self, _id=0, _rarity=1):
        super().__init__()
        self.id = _id
        self.rarity = _rarity
        self.key = 'Super Amulet'
        self.mana = random.randrange(-(self.rarity * 4), -(self.rarity * 2), 1)
        self.passive_skills.extend(self.passive_super_magic_amulet)
        self.active_skills.extend(self.active_super_magic_amulet)
