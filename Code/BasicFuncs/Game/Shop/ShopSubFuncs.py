class ShopChecker:
    def __init__(self):
        pass

    @staticmethod
    def possible_to_buy(gold, cost):
        if gold - cost < 0:
            return False
        return True

    @staticmethod
    def add(obj_dict, obj):
        if obj_dict.get(obj) is None:
            obj_dict[obj] = []
        return obj_dict
