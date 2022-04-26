from Code.Checking.Errors import ImpossibleChange


class CheckAdventurerFuncs:

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


class CheckSkills:

    def __init__(self):
        pass

    @staticmethod
    def battle_params_change(param, val):
        if param - val > 0.000000001:
            return param - val
        else:
            return 0
