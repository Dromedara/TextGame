from Code.Subfunctions.Errors import NoHP


class Checker:

    def __init__(self):
        pass

    @staticmethod
    def params_change(param, val):
        if param + val > 0.000000001:
            return param + val
        else:
            return 0

    @staticmethod
    def hp_change(param, val):
        if param + val > 0.000000001:
            return param + val
        else:
            raise NoHP

    @staticmethod
    def check_hp(hero, monster):
        if hero.hp <= 0:
            raise NoHP
        if monster.hp <= 0:
            return True
        return False

    @staticmethod
    def tiks_add(tiks, key):
        if tiks.get(key) is None:
            tiks[key] = 0
        return tiks

    @staticmethod
    def skills_add(skills, key):
        if skills.get(key) is None:
            skills[key] = []
        return skills


class Show:

    @staticmethod
    def show_hero(hero):
        print(hero.hero_active_skills)
        print(hero.hero_passive_skills)
        print(
            f"hp: {hero.hp},\nattack: {hero.attack},\ndefence: {hero.defence},\nmana: {hero.mana},\nmagic attack: {hero.magic_attack}\n")


class End:
    @staticmethod
    def end_it():
        pass
