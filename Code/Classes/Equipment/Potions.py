from Code.Subfunctions.HelperFunc import ForArtefacts


class Potion:

    key: str
    rarity: int
    attack: float
    defence: float
    hp: float
    mana: float
    magic_attack: float

    def __init__(self):
        self.rarity = 0
        self.attack = 0
        self.defence = 0
        self.hp = 0
        self.mana = 0
        self.magic_attack = 0


class HealingPotion(Potion):

    def __init__(self, _rarity=1, hp=-1, **kwargs):
        super().__init__()
        self.key = 'healing_potion'
        self.rarity = _rarity
        self.hp = ForArtefacts.check_input_data(hp, self.rarity+1, self.rarity+3)


class BoostingPotion(Potion):

    def __init__(self, _rarity, hp=-1, attack=-1, **kwargs):
        super().__init__()
        self.key = 'boosting_potion'
        self.rarity = _rarity
        self.hp = ForArtefacts.check_input_data(hp, self.rarity+1, self.rarity+3)
        self.attack = ForArtefacts.check_input_data(attack, self.rarity+1, self.rarity+3)
