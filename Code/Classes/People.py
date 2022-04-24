import random
import Code.Checking.CheckClassFunctions


class Human:

    name: str

    def __init__(self, _name='?'):
        self.name = _name


class Adventurer(Human):

    lvl: int
    gold: int
    exp: int
    lvl_changing_edge: int
    rise_coeff: float

    power: float
    speed: float
    wisdom: float
    intellect: float
    endurance: float

    attack_coeff: float
    defence_coeff: float
    hp_coeff: float
    mana_coeff: float

    active_skills = []
    passive_skills = []

    checker = Code.Checking.CheckClassFunctions.CheckAdventurerFuncs()

    def __init__(self, _name='?', lvl=1, gold=10, exp=0, lvl_ch_ed=5, rise_coeff=2, power=1, speed=1, wisdom=1, intellect=1, endurance=1,
                 attack_coeff=1.5, defence_coeff=1.5, hp_coeff=1.5, mana_coeff=1.5):

        super().__init__(_name)
        self.lvl = lvl
        self.gold = gold
        self.exp = exp
        self.lvl_changing_edge = lvl_ch_ed
        self.rise_coeff = rise_coeff

        self.power = power
        self.speed = speed
        self.wisdom = wisdom
        self.endurance = endurance
        self.intellect = intellect

        self.attack_coeff = attack_coeff
        self.defence_coeff = defence_coeff
        self.hp_coeff = hp_coeff
        self.mana_coeff = mana_coeff

        self.active_skills = []
        self.passive_skills = []

    def power_change(self, val):
        self.power += val

    def speed_change(self, val):
        self.speed += val

    def endurance_change(self, val):
        self.endurance += val

    def wisdom_change(self, val):
        self.wisdom += val

    def intellect_change(self, val):
        self.intellect += val

    def param_increase(self, lvl):
        self.power_change(lvl)
        self.speed_change(lvl)
        self.endurance_change(lvl)
        self.wisdom_change(lvl)
        self.intellect_change(lvl)

    def change_lvl(self):
        self.exp = self.exp - self.lvl_changing_edge
        self.lvl_changing_edge *= self.rise_coeff
        self.param_increase(self.lvl)

    def change_exp(self, val):
        self.exp = self.checker.possible_change(self.exp, val)
        if self.checker.exp_change(self.exp, self.lvl_changing_edge):
            self.change_lvl()

    def add_active_skill(self, name_of_skill=''):
        self.active_skills.append(name_of_skill)

    def add_passive_skill(self, name_of_skill=''):
        self.passive_skills.append(name_of_skill)


class Merchant(Human):

    decency: int

    def __init__(self, _name='?'):
        super().__init__()
        self.name = _name
        self.decency = random.randrange(0, 100, 1)
