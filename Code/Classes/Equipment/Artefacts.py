from Code.Subfunctions.HelperFunc import ForArtefacts


class Artefact:

    id: int
    rarity: int
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

    def __init__(self, _id=0, _rarity=1, defence=-1, **kwargs):
        super().__init__()
        self.id = _id
        self.rarity = _rarity
        self.key = 'simple_iron_armor'
        self.defence = ForArtefacts.check_input_data(defence, self.rarity, self.rarity * 3)


class CharmedIronArmor(SimpleIronArmor):

    passive_charmed_iron_armor = ['simple_passive_attack']

    def __init__(self, _id=0, _rarity=1, defence=-1, mana=-1, magic_atack=-1, **kwargs):
        super().__init__()
        self.id = _id
        self.rarity = _rarity
        self.key = 'charmed_iron_armor'
        self.defence = ForArtefacts.check_input_data(defence, self.rarity * 5, self.rarity * 10)

        self.mana = ForArtefacts.check_input_data(mana, -(self.rarity * 2), -self.rarity)
        self.magic_attack = ForArtefacts.check_input_data(magic_atack, self.rarity * 2, self.rarity * 3)
        self.passive_skills.extend(self.passive_charmed_iron_armor)


class SimpleSword(Artefact):

    active_simple_sword_skills = ['straight_sword_attack']

    def __init__(self, _id=0, _rarity=1, attack=-1, **kwargs):
        super().__init__()
        self.id = _id
        self.rarity = _rarity
        self.key = 'simple_sword'
        self.attack = ForArtefacts.check_input_data(attack, self.rarity, self.rarity * 2)
        self.active_skills.extend(self.active_simple_sword_skills)


class CharmedSword(SimpleSword):

    active_charmed_sword_skills = ['forced_sword_attack', 'charmed_sword_attack']

    def __init__(self, _id=0, _rarity=1, attack=-1, magic_attack=-1, **kwargs):
        super().__init__()
        self.id = _id
        self.rarity = _rarity
        self.key = 'charmed_sword'
        self.attack = ForArtefacts.check_input_data(attack, self.rarity * 2, self.rarity * 4)
        self.magic_attack = ForArtefacts.check_input_data(magic_attack, self.rarity, self.rarity * 2)
        self.active_skills.extend(self.active_charmed_sword_skills)


class SimpleMagicAmulet(Artefact):

    passive_simple_magic_amulet = ['simple_magic_baff']

    def __init__(self, _id=0, _rarity=1, mana=-1, **kwargs):
        super().__init__()
        self.id = _id
        self.rarity = _rarity
        self.key = 'simple_amulet'
        self.mana = ForArtefacts.check_input_data(mana, -(self.rarity * 3), -self.rarity)
        self.passive_skills.extend(self.passive_simple_magic_amulet)


class SuperMagicAmulet(SimpleMagicAmulet):
    passive_super_magic_amulet = ['super_magic_baff']
    active_super_magic_amulet = ['super_magic_attack']

    def __init__(self, _id=0, _rarity=1, mana=-1, **kwargs):
        super().__init__()
        self.id = _id
        self.rarity = _rarity
        self.key = 'super_amulet'
        self.mana = ForArtefacts.check_input_data(mana, -(self.rarity * 4), -(self.rarity * 2))
        self.passive_skills.extend(self.passive_super_magic_amulet)
        self.active_skills.extend(self.active_super_magic_amulet)
