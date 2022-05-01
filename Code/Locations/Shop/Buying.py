import Code.Locations.Shop.CreateStaff as CreateStaff
from Code.Locations.Shop.ShopSubFuncs import Checker
from Code.Subfunctions.Messages.SOS import SOSMessages
import Code.Locations.Warehouse.Equipping as Equipping


def buy_smth(hero):

    selling_artefacts = CreateStaff.create_artefacts(hero.lvl)
    selling_potions = CreateStaff.create_potions(hero.lvl)

    while True:

        print(hero.gold)

        print(f'artefacts, potions or nothing?')

        a = input()

        if a == 'artefacts':
            while True:
                for key in selling_artefacts.keys():
                    print(f'{key}: {selling_artefacts[key].cost}')
                print('stop')

                choice = input()
                if choice == 'stop':
                    break
                elif Checker.possible_to_buy(hero.gold, selling_artefacts[choice].cost):
                    Equipping.artefacts_dict = Checker.add(Equipping.artefacts_dict, choice)
                    Equipping.artefacts_dict[choice].append(selling_artefacts[choice])
                    hero.gold -= selling_artefacts[choice].cost
                else:
                    SOSMessages.not_enough_money()

        elif a == 'potions':
            while True:
                for key in selling_potions.keys():
                    print(f'{key}: {selling_potions[key].cost}')
                print('stop')

                choice = input()
                if choice == 'stop':
                    break
                elif Checker.possible_to_buy(hero.gold, selling_potions[choice].cost):
                    Equipping.potions_dict = Checker.add(Equipping.potions_dict, choice)
                    Equipping.potions_dict[choice] = selling_potions[choice]
                    hero.gold -= selling_potions[choice].cost
                else:
                    SOSMessages.not_enough_money()
        else:
            return hero
