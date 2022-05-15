from Code.BasicFuncs.Game.Shop.ShopSubFuncs import ShopChecker
from Code.BasicFuncs.Game.Warehouse.Inventory.Armor import ArmorInventory
from Code.BasicFuncs.Game.Warehouse.Inventory.Potions import PotionsInventory
from Code.BasicFuncs.Game.Warehouse.Inventory.Artefacts import ArtefactsInventory
import Code.BasicFuncs.Game.Shop.CreateStuf as CreateStuff


def buy_smth(hero):

    selling_artefacts, selling_armors, selling_potions = CreateStuff.start_shop()

    while True:
        print(f'have {hero.gold} gold')

        print(f'artefacts, armor, potions or nothing?')

        print(ArtefactsInventory.artefacts_dict)
        print(ArmorInventory.armor_dict)
        print(PotionsInventory.potions_dict)
        print('!!!!!!!!!')

        a = input()

        if a == 'artefacts':

            selling_artefacts = CreateStuff.artefacts_shop(selling_artefacts=selling_artefacts)

            while True:
                for key in selling_artefacts.keys():
                    print(f'{selling_artefacts[key].key}: {selling_artefacts[key].id}: {selling_artefacts[key].cost}')
                print('stop: -1')

                choice = int(input())
                if choice == -1:
                    break
                elif ShopChecker.possible_to_buy(hero.gold, selling_artefacts[choice].cost):
                    ArtefactsInventory.artefacts_dict[selling_artefacts[choice].id] = selling_artefacts[choice]
                    hero.gold -= selling_artefacts[choice].cost

        elif a == 'armor':
            selling_armors = CreateStuff.armor_shop(selling_armors=selling_armors)

            while True:
                for key in selling_armors['helmet'].keys():
                    print(selling_armors['helmet'][key].key, end = ' ')
                    print(selling_armors['helmet'][key].cost)

                for key in selling_armors['bib'].keys():
                    print(selling_armors['bib'][key].key, end=' ')
                    print(selling_armors['bib'][key].cost)

                for key in selling_armors['pants'].keys():
                    print(selling_armors['pants'][key].key, end=' ')
                    print(selling_armors['pants'][key].cost)
                print('stop (-1)')
                print(selling_armors)
                print('Enter id')

                choice = int(input())
                print(selling_armors['bib'].keys())
                if choice == -1:
                    break
                elif choice in selling_armors['helmet'].keys():
                    if ShopChecker.possible_to_buy(hero.gold, selling_armors['helmet'][choice].cost):
                        ArmorInventory.armor_dict['helmet'][selling_armors['helmet'][choice].id] = \
                            selling_armors['helmet'][choice]

                        hero.gold -= selling_armors['helmet'][choice].cost
                    else:
                        print('impossible')
                elif choice in selling_armors['bib'].keys():
                    if ShopChecker.possible_to_buy(hero.gold, selling_armors['bib'][choice].cost):
                        ArmorInventory.armor_dict['bib'][selling_armors['bib'][choice].id] = \
                            selling_armors['bib'][choice]
                        hero.gold -= selling_armors['bib'][choice].cost
                    else:
                        print('impossible')
                elif choice in selling_armors['pants'].keys():
                    if ShopChecker.possible_to_buy(hero.gold, selling_armors['pants'][choice].cost):
                        ArmorInventory.armor_dict['pants'][selling_armors['pants'][choice].id] = \
                            selling_armors['pants'][choice]
                        hero.gold -= selling_armors['pants'][choice].cost
                    else:
                        print('impossible')
                else:
                    print('wrong key')

        elif a == 'potions':

            selling_potions = CreateStuff.potions_shop(selling_potions=selling_potions)

            print(selling_potions)

            while True:
                for key in selling_potions.keys():
                    print(f'{selling_potions[key].key}, {selling_potions[key].id}: {selling_potions[key].cost}')
                print('stop -1')

                choice = int(input())
                if choice == -1:
                    break
                elif ShopChecker.possible_to_buy(hero.gold, selling_potions[choice].cost):
                    PotionsInventory.potions_dict = ShopChecker.add(PotionsInventory.potions_dict,
                                                                    selling_potions[choice].key)
                    PotionsInventory.potions_dict[selling_potions[choice].key].append(selling_potions[choice])
                    hero.gold -= selling_potions[choice].cost
        else:
            return hero
