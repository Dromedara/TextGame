from Code.Data.InOutData import PassData


class Finisher:

    @staticmethod
    def lets_finish(hero, artefacts, potions):

        PassData.main_hero(hero)

        PassData.artefacts(artefacts)

        PassData.potions(potions)
