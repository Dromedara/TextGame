class ActiveSkills:

    def __init__(self):
        pass

    @staticmethod
    def straight_sword_attack(hero, monster):
        monster.hp -= (hero.attack - 0.6 * monster.defence)
        monster.defence -= 0.1 * hero.attack
        hero.hp -= 1
        return hero, monster

    @staticmethod
    def forced_sword_attack(hero, monster):
        monster.hp -= (hero.attack - 0.3 * monster.defence)
        monster.defence -= 0.2 * hero.attack
        hero.hp -= 1.2
        return hero, monster

    @staticmethod
    def super_magic_attack(hero, monster):
        monster.hp -= (hero.attack - 0.3 * monster.defence)
        monster.defence -= 0.2 * hero.attack
        hero.mana -= 1.2
        return hero, monster


class PassiveSkills:

    def __init__(self):
        pass

    @staticmethod
    def passive_magic_attack(hero, monster):
        monster.hp -= 1
        return hero, monster

    @staticmethod
    def simple_magic_baff(hero, monster):
        hero.hp += 1
        return hero, monster
