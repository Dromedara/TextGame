import random

from Code.BasicFuncs.Game.BattelField.Prepare.BattleMod import BattleMod
from Code.BasicFuncs.Game.BattelField.Prepare.WearArmor import Wearing
from Code.BasicFuncs.Game.BattelField.Prepare.GetArtefacts import Getting
from Code.BasicFuncs.Game.BattelField.Prepare.DrinkingPotions import Drinking

from Code.BasicFuncs.DataOperations.GetData import monster_creator

import Code.Classes.MainHero.AdventurerLinks as AdventurerLinks
import Code.Classes.Equipment.ArtefactsService.ArtefactsLinks as ArtefactsLinks
import Code.Classes.Monster.MonsterLinks as MonsterLinks

from Code.BasicFuncs.Game.Warehouse.Inventory import Battle

from Code.BasicFuncs.Game.BattelField.BattleSubFuncs import BattleChecker


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
            print(Battle.battle_inventory.curr_potions)

            choice = int(input())

            if choice == -1:
                break
            hero = Drinking.drink_potion(hero, Battle.battle_inventory.curr_potions[choice])
            Battle.done_potions.append(choice)
            del Battle.battle_inventory.curr_potions[choice]

        return hero


class PassiveActions:

    @staticmethod
    def run_it(hero, monster):

        for skill in hero.hero_passive_skills['basic']:
            hero, monster = AdventurerLinks.passive_adventurer_dict[skill](hero, monster)
            BattleChecker.check_hp(hero, monster)

        for skill in hero.hero_passive_skills['artefacts']:
            hero, monster = ArtefactsLinks.passive_artefact_dict[skill](hero, monster)
            BattleChecker.check_hp(hero, monster)

        return hero, monster


class ActiveActions:

    @staticmethod
    def run_it(hero, monster):
        print(hero.hero_active_skills)

        choice = input()

        if choice in ArtefactsLinks.active_artefact_dict.keys():
            hero, monster = ArtefactsLinks.active_artefact_dict[choice](hero, monster)
        else:
            hero, monster = AdventurerLinks.active_adventurer_dict[choice](hero, monster)

        BattleChecker.check_hp(hero, monster)
        return hero, monster


class MonsterActions:

    @staticmethod
    def run_it(hero, monster):
        monster = MonsterActions.passive(monster)
        BattleChecker.check_hp(hero, monster)
        hero, monster = MonsterActions.active(hero, monster)
        BattleChecker.check_hp(hero, monster)
        return hero, monster

    @staticmethod
    def passive(monster):
        for action in monster.passive_skill:
            monster = MonsterLinks.passive_skills_dict[action](monster)
        return monster

    @staticmethod
    def active(hero, monster):
        action = random.randrange(0, len(monster.active_skill), 1)
        return MonsterLinks.active_skills_dict[monster.active_skill[action]](hero, monster)
