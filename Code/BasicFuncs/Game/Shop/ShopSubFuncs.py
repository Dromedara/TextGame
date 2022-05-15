class ShopChecker:
    def __init__(self):
        pass

    @staticmethod
    def possible_to_buy(gold, cost):
        if gold - cost < 0:
            return False
        return True
