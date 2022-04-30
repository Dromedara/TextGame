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
    def tiks_add(tiks, key):
        if tiks.get(key) is None:
            tiks[key] = 0
        return tiks

    @staticmethod
    def protection_change(val, edge):
        if val < edge:
            return edge
        return val