import Code.BasicFuncs.Game.Warehouse.Inventory.Battle as BattleInventory
import Code.BasicFuncs.Game.Warehouse.Inventory.Main as MainInventory


class Choose:

    @staticmethod
    def take_artefact(artefact_id):
        BattleInventory.battle_inventory.curr_artefacts[artefact_id] = \
            MainInventory.main_inventory.artefacts_dict[artefact_id]

    @staticmethod
    def artefact_off(artefact_id):
        print(*BattleInventory.battle_inventory.curr_artefacts)
        del BattleInventory.battle_inventory.curr_artefacts[artefact_id]

    @staticmethod
    def take_potion(potion_id):
        BattleInventory.battle_inventory.curr_potions[potion_id] = \
            MainInventory.main_inventory.potions_dict[potion_id]

    @staticmethod
    def potion_off(potion_id):
        del BattleInventory.battle_inventory.curr_potions[potion_id]

    @staticmethod
    def take_armor(armor_id):
        part = ''
        for key in MainInventory.main_inventory.armor_dict.keys():
            if armor_id in MainInventory.main_inventory.armor_dict[key].keys():
                part = key
                break
        BattleInventory.battle_inventory.curr_armors[part] = MainInventory.main_inventory.armor_dict[part][armor_id]

    @staticmethod
    def armor_off(armor_id):

        for key in BattleInventory.battle_inventory.curr_armors.keys():
            if BattleInventory.battle_inventory.curr_armors[key] is not None:
                if armor_id == BattleInventory.battle_inventory.curr_armors[key].id:
                    BattleInventory.battle_inventory.curr_armors[key] = None
