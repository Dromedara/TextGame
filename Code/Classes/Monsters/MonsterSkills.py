import random
from Code.Checking.CheckClassFunctions import CheckSkills


class ActiveSkills:

    def __init__(self):
        pass

    @staticmethod
    def strait_physical_attack(hero, monster):
        hero.hp -= (monster.attack - 0.5 * hero.defence)
        hero.defence = CheckSkills.battle_params_change(hero.defence, (monster.lvl % 10) + (monster.lvl/10))
        return hero, monster

    @staticmethod
    def straight_magic_attack(hero, monster):
        hero.hp -= (monster.attack - 0.3 * hero.defence)
        hero.mana = CheckSkills.battle_params_change(hero.mana, (monster.lvl % 10) + (monster.lvl / 10))
        return hero, monster


class PassiveSkills:

    def __init__(self):
        pass

    @staticmethod
    def healing_itself(hero, monster):
        monster.hp += random.randrange(0, 2, 1)
        return hero, monster