from Code.Data.InOutData import GetData
from Code.Subfunctions.Messages import Attention


class Starter:

    @staticmethod
    def lets_start_new():
        hero = GetData.main_hero(0)

        Attention.Mover.first_game_activation()

        return hero, [], []

    @staticmethod
    def lets_start_again():
        hero = GetData.main_hero(1)

        artefacts = GetData.artefacts()

        potions = GetData.potions()

        return hero, artefacts, potions

