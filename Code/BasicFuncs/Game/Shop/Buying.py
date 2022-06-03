from Code.BasicFuncs.Game.Shop.ShopSubFuncs import ShopChecker
from Code.BasicFuncs.Game.Shop.ShopSubFuncs import Saver
from Code.BasicFuncs.Game.Warehouse.Inventory.Main import main_inventory
import Code.BasicFuncs.Game.Shop.CreateStuff as CreateStuff

from Code.Classes.MainHero.Savior import ReadHero

from Code.BasicFuncs.Game.Shop import Sellers


def buy_artefact(artefact_id):
    adventurer = ReadHero.read_it()

    if ShopChecker.possible_to_buy(adventurer.gold, Sellers.selling_artefacts[artefact_id].cost):
        main_inventory.add_artefact(Sellers.selling_artefacts[artefact_id])
        adventurer.gold -= Sellers.selling_artefacts[artefact_id].cost
        keyword = Sellers.selling_artefacts[artefact_id].key
        del Sellers.selling_artefacts[artefact_id]
        Sellers.selling_artefacts = CreateStuff.artefacts_shop(keyword=keyword, selling_artefacts=Sellers.selling_artefacts)
        ReadHero.save_it(hero=adventurer)
        Saver.save_changed_artefacts()


def buy_armor(armor_id):
    adventurer = ReadHero.read_it()
    part = ''
    
    for key in Sellers.selling_armors.keys():
        if armor_id in Sellers.selling_armors[key].keys():
            part = key
            break
    if ShopChecker.possible_to_buy(adventurer.gold, Sellers.selling_armors[part][armor_id].cost):
        main_inventory.add_armor(part, Sellers.selling_armors[part][armor_id])
        adventurer.gold -= Sellers.selling_armors[part][armor_id].cost
        keyword = Sellers.selling_armors[part][armor_id].key
        del Sellers.selling_armors[part][armor_id]
        Sellers.selling_armors = CreateStuff.armor_shop(keyword=keyword, part=part, selling_armors=Sellers.selling_armors)
    
    ReadHero.save_it(hero=adventurer)
    Saver.save_changed_armors()
    

def buy_potion(potion_id):
    adventurer = ReadHero.read_it()
    
    if ShopChecker.possible_to_buy(adventurer.gold, Sellers.selling_potions[potion_id].cost):
        main_inventory.add_potion(Sellers.selling_potions[potion_id])
        adventurer.gold -= Sellers.selling_potions[potion_id].cost
        keyword = Sellers.selling_potions[potion_id].key
        del Sellers.selling_potions[potion_id]
        Sellers.selling_potions = CreateStuff.potions_shop(keyword=keyword, selling_potions=Sellers.selling_potions)

    ReadHero.save_it(hero=adventurer)
    Saver.save_changed_potions()
