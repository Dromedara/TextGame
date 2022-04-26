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

    @staticmethod
    def skills_add(skills, key):
        if skills.get(key) is None:
            skills[key] = []
        return skills


class ForSkills:

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
        if val == -1:
            return random.randrange(_min, _max, 1)
        else:
            return val
