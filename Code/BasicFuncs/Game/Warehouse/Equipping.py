import Code.BasicFuncs.Game.Warehouse.Inventory.Battle as BattleInventory
import Code.BasicFuncs.Game.Warehouse.Inventory.Main as MainInventory
from Code.Classes.Equipment.ArtefactsService import ArtefactsLinks
from Code.Classes.Equipment.ArmorService import ArmorLinks
from Code.Classes.Equipment.PotionsService import PotionsLinks


class Choose:

    @staticmethod
    def choose_artefacts():

        while True:
            print(MainInventory.main_inventory.artefacts_dict)
            print(BattleInventory.battle_inventory.curr_artefacts)
            choice = int(input())
            if choice == -1:
                break
            BattleInventory.battle_inventory.curr_artefacts[choice] = MainInventory.main_inventory.artefacts_dict[choice]

    @staticmethod
    def choose_potions():

        while True:
            print(MainInventory.main_inventory.potions_dict)
            print(BattleInventory.battle_inventory.curr_potions)

            choice = int(input())
            if choice == -1:
                break

            BattleInventory.battle_inventory.curr_potions[choice] = MainInventory.main_inventory.potions_dict[choice]

    @staticmethod
    def choose_armors():

        while True:
            print(MainInventory.main_inventory.armor_dict)
            print(BattleInventory.battle_inventory.curr_armors)

            choice = int(input())
            part = ''

            if choice == -1:
                break

            for key in MainInventory.main_inventory.armor_dict.keys():
                if choice in MainInventory.main_inventory.armor_dict[key].keys():
                    part = key
                    break

            BattleInventory.battle_inventory.curr_armors[part][choice] = MainInventory.main_inventory.armor_dict[part][choice]