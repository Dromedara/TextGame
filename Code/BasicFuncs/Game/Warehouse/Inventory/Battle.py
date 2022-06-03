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

    def get_artefacts(self):
        return self.curr_artefacts.values()

    def get_potions(self):
        return self.curr_potions.values()

    def get_armors(self):
        res = []

        for key in self.curr_armors.keys():
            if self.curr_armors[key] is not None:
                res.append(self.curr_armors[key])

        return res


battle_inventory = BattleInventory()
