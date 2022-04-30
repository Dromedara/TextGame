import random


class Checker:

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