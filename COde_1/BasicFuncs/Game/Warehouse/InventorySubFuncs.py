class InventoryChecker:

    @staticmethod
    def add_potion(potions, potion_name):
        if potions.get(potion_name) is None:
            potions[potion_name] = []
        return potions
