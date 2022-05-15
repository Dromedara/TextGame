from Code.Classes.MainHero.AdventurerSubFuncs import AdventurerChecker


class Adventurer:

    name: str
    lvl: int
    gold: int
    exp: int
    lvl_changing_edge: int
    rise_coeff: float

    power: float
    speed: float
    wisdom: float
    intellect: float
    stamina: float
    free: float

    attack_coeff: float
    defence_coeff: float
    hp_coeff: float
    mana_coeff: float

    active_skills = []
    passive_skills = []

    def __init__(self,
                 _name: str = '?',
                 lvl: int = 1, exp: int = 0, lvl_ch_ed: int = 5, rise_coeff: float = 2,
                 gold: int = 10,
                 power: int = 1, speed: int = 1, wisdom: int = 1, intellect: int = 1, stamina: int = 1,
                 free: int = 0,
                 attack_coeff: float = 1.5, defence_coeff: float = 1.5, hp_coeff: float = 1.5, mana_coeff: float = 1.5):
        self.name = _name
        self.lvl = lvl
        self.gold = gold
        self.exp = exp
        self.lvl_changing_edge = lvl_ch_ed
        self.rise_coeff = rise_coeff

        self.power = power
        self.speed = speed
        self.wisdom = wisdom
        self.stamina = stamina
        self.intellect = intellect
        self.free = free

        self.attack_coeff = attack_coeff
        self.defence_coeff = defence_coeff
        self.hp_coeff = hp_coeff
        self.mana_coeff = mana_coeff

        self.active_skills = ['simple_punch']
        self.passive_skills = []

    def power_change(self, val):
        self.power += val

    def speed_change(self, val):
        self.speed += val

    def stamina_change(self, val):
        self.stamina += val

    def wisdom_change(self, val):
        self.wisdom += val

    def intellect_change(self, val):
        self.intellect += val

    def free_change(self, lvl):
        self.free += (lvl / 10) + (lvl % 10)

    def change_lvl(self):
        self.exp = self.exp - self.lvl_changing_edge
        self.lvl_changing_edge *= self.rise_coeff
        self.free_change(self.lvl)

    def change_exp(self, val):
        self.exp = AdventurerChecker.exp_change(self.exp, val)
        if AdventurerChecker.exp_change(self.exp, self.lvl_changing_edge):
            self.change_lvl()

    def add_active_skill(self, name_of_skill=''):
        if name_of_skill not in self.active_skills:
            self.active_skills.append(name_of_skill)

    def add_passive_skill(self, name_of_skill=''):
        if name_of_skill not in self.passive_skills:
            self.passive_skills.append(name_of_skill)