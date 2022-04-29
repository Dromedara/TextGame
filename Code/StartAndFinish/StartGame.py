from Code.Data.InOutData import GetData
from Code.Subfunctions.Messages import Attention


class Starter:

    @staticmethod
    def lets_start_new():
        hero = GetData.main_hero(0)

        Attention.Mover.first_game_activation()

        return hero