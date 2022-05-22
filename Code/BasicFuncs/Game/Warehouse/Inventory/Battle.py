import Code.Classes.Equipment.ArmorService.ArmorLinks as ArmorLinks


done_potions = []


class BattleInventory:

    curr_artefacts: {}
    curr_potions: {}
    curr_armors: {}

    def __init__(self):
        self.done = []
        self.curr_artefacts = {}
        self.curr_potions = {}
        self.curr_armors = {}
        for key in ArmorLinks.parts_dict.keys():
            self.curr_armors[key] = None

    def add_artefact(self, artefact):
        self.curr_artefacts[artefact.id] = artefact

    def add_armor(self, part_name, armor):
        self.curr_armors[part_name][armor.id] = armor

    def add_potion(self, potion):
        self.curr_potions[potion.id] = potion


battle_inventory = BattleInventory()
