import Code.Classes.Equipment.IDCounter as Id
from Code.BasicFuncs.Game.Warehouse.Inventory.Main import main_inventory
from Code.BasicFuncs.Start.GetData import Reset


class RecreateAdventurer:

    @staticmethod
    def get_hero(first_activation=True):
        hero = Reset.adventurer_creator(first_activation=first_activation)
        hero.active_skills, hero.passive_skills = Reset.adventurer_skills(first_activation=first_activation)
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
        main_inventory.artefacts_dict = Reset.artefacts_creator(first_activation=first_activation)

    @staticmethod
    def get_armors(first_activation=True):
        main_inventory.armor_dict = Reset.armors_creator(first_activation=first_activation)

    @staticmethod
    def get_potions(first_activation=True):
        main_inventory.potions_dict = Reset.potions_creator(first_activation=first_activation)

    @staticmethod
    def get_id_counter(first_activation=True):
        Id.id_counter = Reset.id_creator(first_activation=first_activation)
