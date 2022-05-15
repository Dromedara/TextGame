from Code.Classes.Equipment.PotionsService.PotionsSubFuncs import PotionsChecker


class Potion:

    key: str
    id: int
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
        self.id = 0
        self.rarity = 0
        self.tik = 0
        self.cost = 0
        self.attack = 0
        self.defence = 0
        self.hp = 0
        self.mana = 0
        self.magic_attack = 0


class HealingPotion(Potion):

    def __init__(self, _id=0, _rarity=1, hp=0, **kwargs):
        super().__init__()
        self.key = 'healing_potion'
        self.id = _id
        self.rarity = _rarity
        self.cost = 5
        self.hp += PotionsChecker.check_input_data(hp, self.rarity+1, self.rarity+3)


class BoostingPotion(Potion):

    def __init__(self, _id=0, _rarity=1, attack=0, defence=0, **kwargs):
        super().__init__()
        self.key = 'boosting_potion'
        self.id = _id
        self.rarity = _rarity
        self.cost = 5
        self.attack += PotionsChecker.check_input_data(attack, self.rarity+1, self.rarity+3)
        self.defence += PotionsChecker.check_input_data(defence, self.rarity+1, self.rarity+3)


class ProtectingPotion(Potion):

    def __init__(self, _id=0, _rarity=1, _tik=1, **kwargs):
        super().__init__()
        self.key = 'protecting_potion'
        self.id = _id
        self.rarity = _rarity
        self.tik = _tik
        self.cost = 5

    @staticmethod
    def super_protector(hero, val):
        hero.attack = PotionsChecker.protection_change(hero.attack, hero.param_savior['attack'][-val])
        hero.defence = PotionsChecker.protection_change(hero.defence, hero.param_savior['defence'][-val])
        hero.hp = PotionsChecker.protection_change(hero.hp, hero.param_savior['hp'][-val])
        hero.mana = PotionsChecker.protection_change(hero.mana, hero.param_savior['mana'][-val])
        hero.magic_attack = PotionsChecker.protection_change(hero.magic_attack, hero.param_savior['magic_attack'][-val])

        return hero
