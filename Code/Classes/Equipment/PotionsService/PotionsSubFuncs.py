import random


class PotionsChecker:

    def __init__(self):
        pass

    @staticmethod
    def check_input_data(val, _min, _max):
        if val == 0:
            return random.randrange(_min, _max, 1)
        else:
            return val

    @staticmethod
    def protection_change(val, edge):
        if val < edge:
            return edge
        return val
