import Code.Classes.Equipment.ArmorService.ArmorLinks as ArmorLinks
from Code.BasicFuncs.Game.Warehouse.Inventory import Battle


class MainInventory:

    artefacts_dict: {}
    potions_dict: {}
    armor_dict: {}

    def __init__(self):
        self.artefacts_dict = {}
        self.potions_dict = {}
        self.armor_dict = {}
        for key in ArmorLinks.parts_dict.keys():
            self.armor_dict[key] = {}

    def add_artefact(self, artefact):
        self.artefacts_dict[artefact.id] = artefact

    def add_armor(self, part_name, armor):
        self.armor_dict[part_name][armor.id] = armor

    def add_potion(self, potion):
        self.potions_dict[potion.id] = potion

    def del_potions_done(self):
        for key in Battle.done_potions:
            del self.potions_dict[key]

    def get_artefacts(self):
        return self.artefacts_dict.values()

    def get_potions(self):
        return self.potions_dict.values()

    def get_armors(self):
        return self.artefacts_dict.values()


main_inventory = MainInventory()
