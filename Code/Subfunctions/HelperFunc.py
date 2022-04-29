from Code.Subfunctions.Errors import ImpossibleChange
import random


class ForAdventurerFuncs:

    def __init__(self):
        pass

    @staticmethod
    def possible_change(param, val):
        res = param + val
        if res < 0:
            raise ImpossibleChange
        return res

    @staticmethod
    def exp_change(param, edge):
        if param < edge:
            return False
        return True


class ForShop:
    def __init__(self):
        pass

    @staticmethod
    def possible_to_buy(gold, cost):
        if gold - cost < 0:
            return False
        return True


class ForBattle:

    def __init__(self):
        pass

    @staticmethod
    def battle_params_change(param, val):
        if param - val > 0.000000001:
            return param - val
        else:
            return 0


class ForArtefacts:

    def __init__(self):
        pass

    @staticmethod
    def check_input_data(val, _min, _max):
        if val:
            return random.randrange(_min, _max, 1)
        else:
            return val

    @staticmethod
    def skills_add(skills, key):
        if skills.get(key) is None:
            skills[key] = []
        return skills


class ForPotions:

    def __init__(self):
        pass

    @staticmethod
    def check_input_data(val, _min, _max):
        if val:
            return random.randrange(_min, _max, 1)
        else:
            return val

    @staticmethod
    def tiks_add(tiks, key):
        if tiks.get(key) is None:
            tiks[key] = 0
        return tiks
