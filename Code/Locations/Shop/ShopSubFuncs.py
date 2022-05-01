class Checker:
    def __init__(self):
        pass

    @staticmethod
    def possible_to_buy(gold, cost):
        if gold - cost < 0:
            return False
        return True

    @staticmethod
    def add(artefacts, artefact):
        if artefacts.get(artefact) is None:
            artefacts[artefact] = []
        return artefacts
