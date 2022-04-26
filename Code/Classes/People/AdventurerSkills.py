from Code.Subfunctions.HelperFunc import ForSkills


class ActiveSkills:

    def __init__(self):
        pass

    @staticmethod
    def straight_sword_attack(hero, monster):
        monster.hp -= (hero.attack - 0.5 * monster.defence)
        monster.defence = ForSkills.battle_params_change(monster.defence, 0.3 * hero.attack)
        hero.hp -= 1
        return hero, monster

    @staticmethod
    def forced_sword_attack(hero, monster):
        monster.hp -= (hero.attack - 0.3 * monster.defence)
        monster.defence = ForSkills.battle_params_change(monster.defence, 0.5 * hero.attack)
        hero.hp -= 1.2
        return hero, monster

    @staticmethod
    def super_magic_attack(hero, monster):
        monster.hp -= (hero.attack - 0.3 * monster.defence)
        monster.defence = ForSkills.battle_params_change(monster.defence, 0.5 * hero.attack)
        return hero, monster

    @staticmethod
    def charmed_sword_attack(hero, monster):
        monster.hp -= (hero.attack - 0.2 * monster.defence)
        monster.defence = ForSkills.battle_params_change(monster.defence, 0.3 * hero.attack)

        if hero.mana == 0:
            hero.hp -= 2
        hero.mana = ForSkills.battle_params_change(hero.mana, 0.5)

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
        hero.hp *= 1.2
        return hero, monster
