from Code.BasicFuncs.Game.HelperFuncs.Errors import NotPossibleToUse
import Code.BasicFuncs.DataOperations.SaveData as SaveData


class BattleChecker:

    def __init__(self):
        pass

    @staticmethod
    def use_changes(param, val):
        if param + val > 0.000000001:
            return param + val
        else:
            raise NotPossibleToUse

    @staticmethod
    def params_change(param, val, start_param):
        if param + val > 0.000000001:
            if start_param > param + val:
                return start_param
            return param + val
        else:
            return 0

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


class Saver:

    @staticmethod
    def save_changed_data(hero):
        SaveData.save_hero(hero=hero)
        SaveData.save_artefacts()
        SaveData.save_armors()
        SaveData.save_potions()
