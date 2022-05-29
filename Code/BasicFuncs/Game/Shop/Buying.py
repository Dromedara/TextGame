from Code.BasicFuncs.Game.Shop.ShopSubFuncs import ShopChecker
from Code.BasicFuncs.Game.Shop.ShopSubFuncs import Saver
from Code.BasicFuncs.Game.Warehouse.Inventory.Main import main_inventory
import Code.BasicFuncs.Game.Shop.CreateStuff as CreateStuff

from Code.Classes.MainHero.Savior import ReadHero


def buy_smth():

    selling_artefacts, selling_armors, selling_potions = CreateStuff.start_shop()

    adventurer = ReadHero.read_it()

    while True:

        # s
        print(f'have {adventurer.gold} gold')

        print(f'artefacts, armor, potions or nothing?')

        print(main_inventory.artefacts_dict)
        print(main_inventory.armor_dict)
        print(main_inventory.potions_dict)
        print('!!!!!!!!!')
        # f

        choice = input()

        if choice == 'artefacts':
            buy_artefact(adventurer=adventurer, selling_artefacts=selling_artefacts)
            Saver.save_changed_data()

        elif choice == 'armor':
            buy_armor(adventurer=adventurer, selling_armors=selling_armors)
            Saver.save_changed_data()

        elif choice == 'potions':
            buy_potion(adventurer=adventurer, selling_potions=selling_potions)
            Saver.save_changed_data()

        else:
            ReadHero.save_it()
            return


def buy_artefact(adventurer, selling_artefacts):

    while True:
        print(selling_artefacts)
        choice = int(input())
        if choice == -1:
            break
        elif ShopChecker.possible_to_buy(adventurer.gold, selling_artefacts[choice].cost):
            main_inventory.add_artefact(selling_artefacts[choice])
            adventurer.gold -= selling_artefacts[choice].cost
            keyword = selling_artefacts[choice].key
            del selling_artefacts[choice]

            selling_artefacts = CreateStuff.artefacts_shop(keyword=keyword, selling_artefacts=selling_artefacts)

    return


def buy_armor(adventurer, selling_armors):

    while True:
        print(selling_armors)
        choice = int(input())
        part = ''

        if choice == -1:
            break
        else:

            for key in selling_armors.keys():
                if choice in selling_armors[key].keys():
                    part = key
                    break
            if ShopChecker.possible_to_buy(adventurer.gold, selling_armors[part][choice].cost):
                main_inventory.add_armor(part, selling_armors[part][choice])
                adventurer.gold -= selling_armors[part][choice].cost
                keyword = selling_armors[part][choice].key
                del selling_armors[part][choice]
                selling_armors = CreateStuff.armor_shop(keyword=keyword, part=part, selling_armors=selling_armors)
            else:
                print('impossible')
    return


def buy_potion(adventurer, selling_potions):

    while True:
        print(selling_potions)
        choice = int(input())

        if choice == -1:
            break
        elif ShopChecker.possible_to_buy(adventurer.gold, selling_potions[choice].cost):
            main_inventory.add_potion(selling_potions[choice])
            adventurer.gold -= selling_potions[choice].cost
            keyword = selling_potions[choice].key
            del selling_potions[choice]
            selling_potions = CreateStuff.potions_shop(keyword=keyword, selling_potions=selling_potions)
    return
