from Code.Classes.Equipment.ArmorService.ArmorsSubFunc import ArmorChecker


class ArmorPart:

    id: int
    rarity: int
    cost: int
    key: str
    attack: float
    defence: float
    hp: float
    mana: float
    magic_attack: float
    description: str

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

        self.description = 'Unknown! Be careful!'

        self.active_skills = []
        self.passive_skills = []


class SimpleHelmet(ArmorPart):

    def __init__(self, _id=0, _rarity=1, defence=0, **kwargs):
        super().__init__()
        self.id = _id
        self.rarity = _rarity
        self.key = 'simple_helmet'
        self.description = 'Simple iron helmet.'
        self.cost = self.rarity*5
        self.defence += ArmorChecker.check_input_data(defence, self.rarity*3, self.rarity*5)


class SuperHelmet(SimpleHelmet):

    def __init__(self, _id=0, _rarity=1, defence=0, **kwargs):
        super().__init__()
        self.id = _id
        self.rarity = _rarity
        self.key = 'super_helmet'
        self.description = 'Super metal helmet.'
        self.cost = self.rarity * 5
        self.defence += ArmorChecker.check_input_data(defence, self.rarity*3, self.rarity * 5)


class SimpleBib(ArmorPart):

    def __init__(self, _id=0, _rarity=1, defence=0, **kwargs):
        super().__init__()
        self.id = _id
        self.rarity = _rarity
        self.key = 'simple_bib'
        self.description = 'Simple iron bib.'
        self.cost = self.rarity * 5
        self.defence += ArmorChecker.check_input_data(defence, self.rarity*5, self.rarity * 6)


class CharmedBib(SimpleBib):

    passive_charmed_bib = ['simple_passive_attack']

    def __init__(self, _id=0, _rarity=1, defence=0, mana=0, magic_atack=0, **kwargs):
        super().__init__()
        self.id = _id
        self.rarity = _rarity
        self.cost = self.rarity * 10
        self.key = 'charmed_bib'
        self.description = 'Charmed iron bib.'
        self.defence += ArmorChecker.check_input_data(defence, self.rarity * 5, self.rarity * 10)

        self.mana += ArmorChecker.check_input_data(mana, -(self.rarity * 2), -self.rarity)
        self.magic_attack += ArmorChecker.check_input_data(magic_atack, self.rarity * 2, self.rarity * 3)
        self.passive_skills.extend(self.passive_charmed_bib)

    @staticmethod
    def simple_passive_attack(hero, monster):
        monster.hp -= (hero.attack - 0.9 * monster.defence)
        return hero, monster


class SimplePants(ArmorPart):

    def __init__(self, _id=0, _rarity=1, defence=0, **kwargs):
        super().__init__()
        self.id = _id
        self.rarity = _rarity
        self.key = 'simple_pants'
        self.description = 'Simple pants.'
        self.cost = self.rarity * 5
        self.attack += ArmorChecker.check_input_data(defence, self.rarity*2, self.rarity * 3)