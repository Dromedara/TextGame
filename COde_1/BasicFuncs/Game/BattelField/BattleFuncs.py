from COde_1.BasicFuncs.Game.BattelField.Prepare.BattleMod import BattleMod
from COde_1.BasicFuncs.Game.BattelField.Prepare.WearArmor import Wearing
from COde_1.BasicFuncs.Game.BattelField.Prepare.GetArtefacts import Getting
from COde_1.BasicFuncs.Game.BattelField.Prepare.DrinkingPotions import Drinking
import COde_1.BasicFuncs.Game.BattelField.BattleRunner as BattleRunner
import COde_1.BasicFuncs.Game.BattelField.BattleSubFuncs as BattleSubFuncs

import COde_1.Classes.MainHero.AdventurerLinks as AdventurerLinks
import COde_1.Classes.Equipment.ArtefactsService.ArtefactsLinks as ArtefactsLinks


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
            return None
        return choice

    @staticmethod
    def delete_it(choice):
        BattleRunner.curr_potions[choice].pop()

    @staticmethod
    def run_it(hero):

        while True:
            BattleSubFuncs.Show.show_potions()
            choice = PotionsActions.choose_it()
            if choice is None:
                break
            hero = Drinking.drink_potion(hero, choice)
            PotionsActions.delete_it(choice)

        print(hero)

        return hero


class PassiveActions:

    @staticmethod
    def run_it(hero, monster):

        for skill in hero.passive_skills['basic']:
            hero, monster = AdventurerLinks.passive_adventurer_dict[skill](hero, monster)

        for skill in hero.passive_skills['artefacts']:
            hero, monster = ArtefactsLinks.passive_artefact_dict[skill](hero, monster)

        return hero, monster
