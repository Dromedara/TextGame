from Code.Subfunctions.HelperFunc import ForArtefacts


class Potion:

    key: str
    rarity: int
    tik: int

    attack: float
    defence: float
    hp: float
    mana: float
    magic_attack: float

    def __init__(self):
        self.rarity = 0
        self.tik = 0
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
        self.tik = 0
        self.hp = ForArtefacts.check_input_data(hp, self.rarity+1, self.rarity+3)


class BoostingPotion(Potion):

    def __init__(self, _rarity, hp=-1, attack=-1, **kwargs):
        super().__init__()
        self.key = 'boosting_potion'
        self.rarity = _rarity
        self.tik = 0
        self.hp = ForArtefacts.check_input_data(hp, self.rarity+1, self.rarity+3)
        self.attack = ForArtefacts.check_input_data(attack, self.rarity+1, self.rarity+3)


class ProtectingPotion(Potion):

    def __init__(self, _rarity, **kwargs):
        super().__init__()
        self.key = 'protecting_potion'
        self.rarity = _rarity
        self.tik = 4
        self.hp_savior = 0

    def protection_activate(self, hero):
        if self.tik == 3:
            self.hp_savior = hero.hp
            hero.hero_long_baffs.append('protecting_potion')
        elif self.tik == 0:
            del hero.hero_long_baffs['protecting_potion']
        return hero

    def reinstate_hp(self, hero):
        hero.hp = self.hp_savior
        return hero
