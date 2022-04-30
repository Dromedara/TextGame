import Code.Locations.Battle.BattleRunner as BattleRunner


class Checker:

    def __init__(self):
        pass

    @staticmethod
    def battle_params_change(param, val):
        if param - val > 0.000000001:
            return param - val
        else:
            return 0


class Show:

    @staticmethod
    def show_hero(hero):
        print(hero.hero_active_skills)
        print(hero.hero_passive_skills)
        print(
            f"hp: {hero.hp},\nattack: {hero.attack},\ndefence: {hero.defence},\nmana: {hero.mana},\nmagic attack: {hero.magic_attack}\n")

    @staticmethod
    def show_potions():
        print(*BattleRunner.curr_potions.values())



