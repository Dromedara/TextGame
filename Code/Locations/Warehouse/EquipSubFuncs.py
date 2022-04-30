class Checker:

    @staticmethod
    def add_potion(slots, key):
        if slots.get(key) is None:
            slots[key] = []
        return slots
