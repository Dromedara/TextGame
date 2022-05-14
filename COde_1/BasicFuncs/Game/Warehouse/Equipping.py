class Choose:

    @staticmethod
    def get_out_artefact(slots):
        print('Get out something?')

        choice = input()
        if choice == 'armor':
            ButtleRunner.artefacts_dict[choice] = slots['armor']
            slots['armor'] = None
        elif choice == 'sword':
            ButtleRunner.artefacts_dict[choice] = slots['sword']
            slots['sword'] = None
        elif choice == 'amulets':
            choice = input()
            ButtleRunner.artefacts_dict[choice] = slots['amulets']
            slots['amulets'] = 0
        elif choice == 'nothing':
            return slots

    @staticmethod
    def choose_artifacts():

        slots = ArtefactsLinks.artefact_battle_slots

        print(* ButtleRunner.artefacts_dict)

        while True:
            for key in ButtleRunner.artefacts_dict.keys():
                print(key, end=' ')
            print('nothing\n')

            choice = input()
            if choice in ArtefactsLinks.armors:
                slots['armor'] = ButtleRunner.artefacts_dict[choice]
            elif choice in ArtefactsLinks.swords:
                slots['sword'] = ButtleRunner.artefacts_dict[choice]
            elif choice in ArtefactsLinks.amulets:
                slots['amulets'].append(ButtleRunner.artefacts_dict[choice])
            elif choice == 'nothing':
                return slots
            else:
                SOSMessages.no_equip_slot()

            print(slots)

            Choose.get_out_artefact(slots)

    @staticmethod
    def choose_potions():
        slots = PotionsLinks.potions_battle_slots

        while True:
            for key in ButtleRunner.potions_dict.keys():
                print(key, end=' ')
            print('nothing\n')

            choice = input()
            if choice in PotionsLinks.potions_list:
                slots = Checker.add_potion(slots, choice)
                slots[choice].append(ButtleRunner.potions_dict[choice])
            elif choice == 'nothing':
                return slots
            else:
                SOSMessages.no_equip_slot()
