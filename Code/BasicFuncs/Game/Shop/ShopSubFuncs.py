import Code.BasicFuncs.DataOperations.SaveData as SaveData


class ShopChecker:
    def __init__(self):
        pass

    @staticmethod
    def possible_to_buy(gold, cost):
        if gold - cost < 0:
            return False
        return True


class Saver:

    @staticmethod
    def save_changed_artefacts():
        SaveData.save_artefacts()

    @staticmethod
    def save_changed_armors():
        SaveData.save_armors()

    @staticmethod
    def save_changed_potions():
        SaveData.save_potions()
