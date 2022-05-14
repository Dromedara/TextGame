from COde_1.BasicFuncs.Game.Warehouse.Inventory.Armor import ArmorInventory
from COde_1.BasicFuncs.Game.Warehouse.Inventory.Artefacts import ArtefactsInventory
from COde_1.BasicFuncs.Game.Warehouse.Inventory.Potions import PotionsInventory
from COde_1.BasicFuncs.Start.GetData import Reset


class RecreateAdventurer:

    @staticmethod
    def get_hero(first_activation=False):
        hero = Reset.adventurer_creator(first_activation=first_activation)
        hero.active_skills, hero.passive_skills = Reset.adventurer_skills(first_activation=first_activation)
        return hero


class RecreateEquipment:

    @staticmethod
    def get_equip(first_activation=False):
        RecreateEquipment.get_armors(first_activation)
        RecreateEquipment.get_artefacts(first_activation)
        RecreateEquipment.get_potions(first_activation)

    @staticmethod
    def get_artefacts(first_activation=False):
        ArtefactsInventory.artefacts_dict = Reset.artefacts_creator(first_activation=first_activation)

    @staticmethod
    def get_armors(first_activation=False):
        ArmorInventory.armor_dict = Reset.armors_creator(first_activation=first_activation)

    @staticmethod
    def get_potions(first_activation=False):
        PotionsInventory.potions_dict = Reset.potions_creator(first_activation=first_activation)
