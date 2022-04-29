import random
import Code.Subfunctions.HelperFunc
import Code.Subfunctions.HelperFunc as HelperFunc


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
    stamina: float
    free: float

    attack_coeff: float
    defence_coeff: float
    hp_coeff: float
    mana_coeff: float

    active_skills = []
    passive_skills = []

    checker = Code.Subfunctions.HelperFunc.ForAdventurerFuncs()

    def __init__(self, _name='?', lvl=1, gold=10, exp=0, lvl_ch_ed=5, rise_coeff=2, power=1, speed=1, wisdom=1,
                 intellect=1, stamina=1, free=0, attack_coeff=1.5, defence_coeff=1.5, hp_coeff=1.5, mana_coeff=1.5):

        super().__init__(_name)
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
        self.exp = self.checker.possible_change(self.exp, val)
        if self.checker.exp_change(self.exp, self.lvl_changing_edge):
            self.change_lvl()

    def add_active_skill(self, name_of_skill=''):
        if name_of_skill not in self.active_skills:
            self.active_skills.append(name_of_skill)

    def add_passive_skill(self, name_of_skill=''):
        if name_of_skill not in self.passive_skills:
            self.passive_skills.append(name_of_skill)


class AdventurerFuncs:

    @staticmethod
    def simple_punch(hero, monster):
        monster.hp -= (hero.attack - 0.8 * monster.defence)
        monster.defence = HelperFunc.ForBattle.battle_params_change(monster.defence, 0.2 * hero.attack)
        return hero, monster
