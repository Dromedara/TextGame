

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
        self.key = ''
        self.attack = 0
        self.defence = 0
        self.hp = 0
        self.mana = 0
        self.magic_attack = 0

        self.active_skills = []
        self.passive_skills = []


class SimpleIronArmor(Artefact):

    def __init__(self):
        super().__init__()
        self.key = 'Simple Iron Armor'
        self.defence = 5


class CharmedIronArmor(SimpleIronArmor):

    passive_charmed_iron_armor = ['simple passive attack']

    def __init__(self):
        super().__init__()
        self.key = 'Charmed Iron Armor'
        self.defence = 15
        self.mana = -2
        self.magic_attack = 5
        self.passive_skills.extend(self.passive_charmed_iron_armor)


class SimpleSword(Artefact):

    active_simple_sword_skills = ['straight sword attack']

    def __init__(self):
        super().__init__()
        self.key = 'Simple Sword'
        self.attack = 5
        self.active_skills.extend(self.active_simple_sword_skills)


class CharmedSword(SimpleSword):

    active_charmed_sword_skills = ['forced sword attack']

    def __init__(self):
        super().__init__()
        self.key = 'Charmed Sword'
        self.attack = 10
        self.active_skills.extend(self.active_charmed_sword_skills)


class SimpleMagicAmulet(Artefact):

    passive_simple_magic_amulet = ['simple magic baff']

    def __init__(self):
        super().__init__()
        self.key = 'Simple Amulet'
        self.mana -= 1
        self.passive_skills.extend(self.passive_simple_magic_amulet)


class SuperMagicAmulet(SimpleMagicAmulet):
    passive_super_magic_amulet = ['super magic baff']
    active_super_magic_amulet = ['super magic attack']

    def __init__(self):
        super().__init__()
        self.key = 'Super Amulet'
        self.mana -= 2
        self.passive_skills.extend(self.passive_super_magic_amulet)
        self.active_skills.extend(self.active_super_magic_amulet)
