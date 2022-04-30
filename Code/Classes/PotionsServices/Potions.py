from Code.Subfunctions.HelperFunc import ForPotions


class Potion:

    key: str
    rarity: int
    tik: int
    cost: int

    attack: float
    defence: float
    hp: float
    mana: float
    magic_attack: float

    def __init__(self):
        self.key = ''
        self.rarity = 0
        self.tik = 0
        self.cost = 0
        self.attack = 0
        self.defence = 0
        self.hp = 0
        self.mana = 0
        self.magic_attack = 0


class HealingPotion(Potion):

    def __init__(self, _rarity=1, hp=0, **kwargs):
        super().__init__()
        self.key = 'healing_potion'
        self.rarity = _rarity
        self.cost = 5
        self.hp += ForPotions.check_input_data(hp, self.rarity+1, self.rarity+3)


class BoostingPotion(Potion):

    def __init__(self, _rarity=1, attack=0, defence=0, **kwargs):
        super().__init__()
        self.key = 'boosting_potion'
        self.rarity = _rarity
        self.cost = 5
        self.attack += ForPotions.check_input_data(attack, self.rarity+1, self.rarity+3)
        self.defence += ForPotions.check_input_data(defence, self.rarity+1, self.rarity+3)


class ProtectingPotion(Potion):

    def __init__(self, _rarity=1, _tik=0, **kwargs):
        super().__init__()
        self.key = 'protecting_potion'
        self.rarity = _rarity
        self.tik = _tik
        self.cost = 5

