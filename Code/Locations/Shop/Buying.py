import Code.Locations.Shop.CreateStaff as CreateStaff
from Code.Subfunctions.HelperFunc import ForShop
from Code.Subfunctions.Messages.SOS import SOSMessages


def buy_smth(hero):
    bought_artefacts = {}
    bought_potions = {}

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
                elif ForShop.possible_to_buy(hero.gold, selling_artefacts[choice].cost):
                   bought_artefacts[choice] = selling_artefacts[choice]
                   hero.gold -= selling_artefacts[choice].cost
                   del selling_artefacts[choice]
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
                elif ForShop.possible_to_buy(hero.gold, selling_potions[choice].cost):
                    bought_potions[choice] = selling_potions[choice]
                    hero.gold -= selling_potions[choice].cost
                    del selling_potions[choice]
                else:
                    SOSMessages.not_enough_money()
        else:
            return hero, bought_artefacts, bought_potions
