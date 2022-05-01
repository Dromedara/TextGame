from Code.Data.InOutData import PassData
import Code.Locations.Warehouse.Equipping as Equipping


class Finisher:

    @staticmethod
    def lets_finish(hero):

        PassData.main_hero(hero)

        PassData.artefacts(Equipping.artefacts_dict)

        PassData.potions(Equipping.potions_dict)
