import Code.ArtefactsServices.ArtefactsLinks as ArtefactsLinks
from Code.Subfunctions.Messages.SOS import SOSMessages


class Choose:

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
                slots['amulet'] = artefacts[choice]
            elif choice == 'noting':
                return slots
            else:
                SOSMessages.no_equip_slot()
                return slots



