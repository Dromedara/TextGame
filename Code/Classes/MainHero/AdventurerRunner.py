from Code.Classes.MainHero.AdventurerSubFuncs import AdventurerChecker


class Adventurer:
    """Main hero of  this game.

    """

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
    free: int

    attack_coeff: float
    defence_coeff: float
    hp_coeff: float
    mana_coeff: float

    active_skills = []
    passive_skills = []

    def __init__(self,
                 _name: str = '?',
                 lvl: int = 1, exp: int = 0, lvl_ch_ed: int = 10, rise_coeff: float = 2,
                 gold: int = 10,
                 power: float = 10, speed: float = 10, wisdom: float = 10, intellect: float = 10, stamina: float = 10,
                 free: int = 0,
                 attack_coeff: float = 1.5, defence_coeff: float = 1.5, hp_coeff: float = 1.5, mana_coeff: float = 1.5):

        """Initialize the hero.

        :param _name: name of the hero
        :param lvl: level of him
        :param exp: experience points
        :param lvl_ch_ed: how much exp should have for rising to the next level
        :param rise_coeff: coefficient for changing lvl_ch_ed by multiplying
        :param gold: money
        :param power: strenght of hero
        :param speed: speed of movements
        :param wisdom: wisdom of hero
        :param intellect: intellect of hero
        :param stamina: stamina of hero
        :param free: free points for increasing power/speed/wisdom/intellect/stamina
        :param attack_coeff: coefficiet for creating battle params
        :param defence_coeff: coefficiet for creating battle params
        :param hp_coeff: coefficiet for creating battle params
        :param mana_coeff: coefficiet for creating battle params


        """

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
        """Changing param "power"

        :param val: val for changing
        :return: None

        """
        self.power += val

    def speed_change(self, val):
        """Changing param "speed"

        :param val: val for changing
        :return: None

        """
        self.speed += val

    def stamina_change(self, val):
        """Changing param "stamina"

        :param val: val for changing
        :return: None

        """
        self.stamina += val

    def wisdom_change(self, val):
        """Changing param "wisdom"

        :param val: val for changing
        :return: None

        """
        self.wisdom += val

    def intellect_change(self, val):
        """Changing param "speed"

        :param val: val for changing
        :return: None

        """
        self.intellect += val

    def free_change(self, lvl):
        """Changing param "speed"

        :param lvl: val for changing (lvl of hero)
        :return: None

        """
        self.free += (lvl / 10) + (lvl % 10)

    def change_lvl(self):
        """Changing lvl of hero

        :return: None
        """
        print("NEXT LVL")
        self.exp = self.exp - self.lvl_changing_edge
        self.lvl_changing_edge *= self.rise_coeff
        self.free_change(self.lvl)

    def change_exp(self, val):
        """Change experience points and activate changing lvl if it is needed

        :param val: val for changing
        :return: None
        """
        self.exp = AdventurerChecker.exp_change(self.exp, val)
        if AdventurerChecker.exp_change(self.exp, self.lvl_changing_edge):
            self.change_lvl()

    def add_active_skill(self, name_of_skill=''):
        """Add basic active skill

        :param name_of_skill: name o added skill
        :return: None
        """
        if name_of_skill not in self.active_skills:
            self.active_skills.append(name_of_skill)

    def add_passive_skill(self, name_of_skill=''):
        """Add basic passive skill

        :param name_of_skill: name of added skill
        :return: None
        """
        if name_of_skill not in self.passive_skills:
            self.passive_skills.append(name_of_skill)
