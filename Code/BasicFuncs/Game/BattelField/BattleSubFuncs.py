from Code.BasicFuncs.Game.HelperFuncs.Errors import NoHP
from Code.BasicFuncs.Game.HelperFuncs.Errors import MonsterDied
from Code.BasicFuncs.Game.HelperFuncs.Errors import NotPossibleToUse
import Code.BasicFuncs.DataOperations.SaveData as SaveData

class BattleChecker:

    def __init__(self):
        pass

    @staticmethod
    def params_change(param, val):
        if param + val > 0.000000001:
            return param + val
        else:
            raise NotPossibleToUse

    @staticmethod
    def hp_change(param, val):
        if param + val > 0.000000001:
            return param + val
        else:
            raise NoHP

    @staticmethod
    def check_hp(hero, monster):
        if monster.hp <= 0.0000000001:
            raise MonsterDied
        if hero.hp <= 0.0000000001:
            raise NoHP

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


class Saver:

    @staticmethod
    def save_changed_data(hero):
        SaveData.save_hero(hero=hero)
        SaveData.save_artefacts()
        SaveData.save_armors()
        SaveData.save_potions()
