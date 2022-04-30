import Code.Classes.ArtefactsServices.ArtefactsLinks as ArtefactsLinks
import Code.Classes.PotionsServices.PotionsLinks as PotionsLinks
from Code.Subfunctions.Messages.SOS import SOSMessages
from Code.Locations.Warehouse.EquipSubFuncs import Checker

artefacts_list = []


potions_list = []


class Choose:

    @staticmethod
    def get_out_artefact(slots):
        print('Get out something?')

        choice = input()
        if choice == 'armor':
            slots['armor'] = None
        elif choice == 'sword':
            slots['sword'] = None
        elif choice == 'amulets':
            choice = input()
            slots['amulet'].pop(slots['amulet'].index(choice))
        elif choice == 'noting':
            return slots

    @staticmethod
    def choose_artifacts(artefacts):

        slots = ArtefactsLinks.artefact_battle_slots

        while True:
            for key in artefacts.keys():
                print(key, end=' ')
            print('nothing\n')

            choice = input()
            if choice in ArtefactsLinks.armors:
                slots['armor'] = artefacts[choice]
            elif choice in ArtefactsLinks.swords:
                slots['sword'] = artefacts[choice]
            elif choice in ArtefactsLinks.amulets:
                slots['amulet'].append(artefacts[choice])
            elif choice == 'noting':
                return slots
            else:
                SOSMessages.no_equip_slot()

            print(slots)

            Choose.get_out_artefact(slots)

    @staticmethod
    def choose_potions(potions):
        slots = PotionsLinks.potions_battle_slots

        while True:
            for key in potions.keys():
                print(key, end=' ')
            print('nothing\n')

            choice = input()
            if choice in PotionsLinks.potions_list:
                slots = Checker.add_potion(slots, choice)
                slots[choice].append(potions[choice])
            elif choice == 'noting':
                return slots
            else:
                SOSMessages.no_equip_slot()
