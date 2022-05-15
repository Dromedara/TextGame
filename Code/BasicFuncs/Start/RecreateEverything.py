import Code.Classes.Equipment.IDCounter as Id
from Code.BasicFuncs.Game.Warehouse.Inventory.Main import main_inventory
from Code.BasicFuncs.DataOperations import GetData


class RecreateAdventurer:

    @staticmethod
    def get_hero(first_activation=True):
        hero = GetData.adventurer_creator(first_activation=first_activation)
        hero.active_skills, hero.passive_skills = GetData.adventurer_skills(first_activation=first_activation)
        return hero


class RecreateEquipment:

    @staticmethod
    def get_equip(first_activation=True):
        RecreateEquipment.get_armors(first_activation)
        RecreateEquipment.get_artefacts(first_activation)
        RecreateEquipment.get_potions(first_activation)
        RecreateEquipment.get_id_counter(first_activation)

    @staticmethod
    def get_artefacts(first_activation=True):
        main_inventory.artefacts_dict = GetData.artefacts_creator(first_activation=first_activation)

    @staticmethod
    def get_armors(first_activation=True):
        main_inventory.armor_dict = GetData.armors_creator(first_activation=first_activation)

    @staticmethod
    def get_potions(first_activation=True):
        main_inventory.potions_dict = GetData.potions_creator(first_activation=first_activation)

    @staticmethod
    def get_id_counter(first_activation=True):
        Id.id_counter = GetData.id_creator(first_activation=first_activation)
