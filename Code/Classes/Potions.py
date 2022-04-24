class Potion:

    attack: float
    defence: float
    hp: float
    mana: float
    magic_attack: float

    def __init__(self):
        self.attack = 0
        self.defence = 0
        self.hp = 0
        self.mana = 0
        self.magic_attack = 0


class HealingPotion(Potion):

    def __init__(self):
        super().__init__()
        self.hp = 3


class BoostingPotion(Potion):

    def __init__(self):
        super().__init__()
        self.hp = -2
        self.attack = 10
