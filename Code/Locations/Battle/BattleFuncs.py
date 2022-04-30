from Code.Classes.MainCharacter.BattleMod import BattleMod
from Code.Classes.ArtefactsServices.WearingArtefacts import Wearing
from Code.Classes.PotionsServices.DrinkingPotions import Drinking
import Code.Locations.Battle.BattleRunner as BattleRunner
import Code.Locations.Battle.BattleSubFuncs as BattleSubFuncs
from Code.Data.InOutData import GetData


class Other:
    @staticmethod
    def check(hero, monster):
        if hero.hp <= 0 or monster.hp <= 0:
            return True
        return False


class Prepearing:
    @staticmethod
    def prepare_hero(adventurer):

        hero = BattleMod(adventurer)

        if BattleRunner.curr_artefacts['armor'] is not None:
            hero = Wearing.get_equipment(hero, BattleRunner.curr_artefacts['armor'])
        if BattleRunner.curr_artefacts['sword'] is not None:
            hero = Wearing.get_equipment(hero, BattleRunner.curr_artefacts['sword'])
        for amulet in BattleRunner.curr_artefacts['amulets']:
            hero = Wearing.get_equipment(hero, amulet)

        return hero

    @staticmethod
    def prepare_monster(adventure_name, serial_num=1):

        monster = GetData.monster(adventure_name=adventure_name, serial_num=serial_num)

        return monster


class PotionsActions:

    @staticmethod
    def choose_it():
        choice = input()
        if choice == 'nothing':
            return False
        return choice

    @staticmethod
    def run_it(hero):

        while True:
            BattleSubFuncs.Show.show_potions()
            if PotionsActions.choose_it():
                break
            hero = Drinking.drink_potion(hero, )

