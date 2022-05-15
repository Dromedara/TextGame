from Code.BasicFuncs.Game.BattelField.Prepare.BattleMod import BattleMod
from Code.BasicFuncs.Game.BattelField.Prepare.WearArmor import Wearing
from Code.BasicFuncs.Game.BattelField.Prepare.GetArtefacts import Getting
from Code.BasicFuncs.Game.BattelField.Prepare.DrinkingPotions import Drinking

import Code.BasicFuncs.Game.BattelField.BattleRunner as BattleRunner
import Code.BasicFuncs.Game.BattelField.BattleSubFuncs as BattleSubFuncs

from Code.BasicFuncs.Start.GetData.Reset import monster_creator

import Code.Classes.MainHero.AdventurerLinks as AdventurerLinks
import Code.Classes.Equipment.ArtefactsService.ArtefactsLinks as ArtefactsLinks

from Code.BasicFuncs.Game.Warehouse.Inventory import Battle


class Preparing:
    @staticmethod
    def prepare_hero(adventurer):

        hero = BattleMod(adventurer)

        hero = Preparing.prepare_armor(hero)

        hero = Preparing.prepare_artefacts(hero)

        return hero

    @staticmethod
    def prepare_armor(hero):

        for part in Battle.battle_inventory.curr_armors.keys():
            if Battle.battle_inventory.curr_armors[part] is not None:
                hero = Wearing.get_equipment(hero, Battle.battle_inventory.curr_armors[part])

        return hero

    @staticmethod
    def prepare_artefacts(hero):
        for key in Battle.battle_inventory.curr_artefacts.keys():
            hero = Getting.get_equipment(hero, Battle.battle_inventory.curr_artefacts[key])
        return hero

    @staticmethod
    def prepare_monster(adventure_name, serial_num=1):

        monster = monster_creator(adventure_name=adventure_name, serial_num=serial_num)

        return monster


class PotionsActions:

    @staticmethod
    def run_it(hero):

        while True:

            choice = input()

            if choice is None:
                break
            hero = Drinking.drink_potion(hero, choice)

        print(hero)

        return hero


class PassiveActions:

    @staticmethod
    def run_it(hero, monster):

        print(hero.hero_passive_skills)

        for skill in hero.hero_passive_skills['basic']:
            hero, monster = AdventurerLinks.passive_adventurer_dict[skill](hero, monster)

        for skill in hero.hero_passive_skills['artefacts']:
            hero, monster = ArtefactsLinks.passive_artefact_dict[skill](hero, monster)

        return hero, monster
