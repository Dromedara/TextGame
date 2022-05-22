from Code.BasicFuncs.Game.BattelField.SubFuncs.BattleMod import BattleMod
from Code.BasicFuncs.Game.BattelField.SubFuncs.WearArmor import Wearing
from Code.BasicFuncs.Game.BattelField.SubFuncs.GetArtefacts import Getting

from Code.BasicFuncs.Game.Warehouse.Inventory import Battle

from Code.BasicFuncs.DataOperations.GetData import monster_creator


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
        print(monster)

        return monster
