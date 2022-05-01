from Code.Data.InOutData import GetData
from Code.Subfunctions.Messages import Attention
from Code.Classes.ArtefactsServices.CreateArtefact import Creator
from Code.Classes.PotionsServices.CreatePotion import Creator
import Code.Locations.Warehouse.Equipping as Equipping


class Starter:

    @staticmethod
    def lets_start_new():
        hero = GetData.main_hero(0)

        Attention.Mover.first_game_activation()

        return hero

    @staticmethod
    def lets_start_again():
        hero = GetData.main_hero(1)

        Equipping.artefacts_dict = GetData.artefacts()

        Equipping.potions_dict = GetData.potions()

        return hero

