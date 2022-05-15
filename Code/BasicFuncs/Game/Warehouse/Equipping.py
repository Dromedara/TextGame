import Code.BasicFuncs.Game.Warehouse.BattleInvetory as BattleInvetory


class Choose:

    @staticmethod
    def choose_artifacts():

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
