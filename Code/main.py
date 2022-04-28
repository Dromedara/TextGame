import Code.Data.InOutData as Data
from Code.Classes.Potions.DrinkingPotions import Drinking
import Code.Classes.Potions.Potions as Potion
from Code.Classes.People.BattleMod import BattleMod
from Code.Classes.People.People import Adventurer


def main():

    # hero = Adventurer()

    hero = Data.GetData.main_hero()

    print(hero.name)

    warr = BattleMod(hero)

    print(warr.tiks)

    potion = Potion.ProtectingPotion(_rarity=1)

    warr = Drinking.drink_potion(warr, potion)
    print(warr.tiks)

    '''    
    potion = HealingPotion()
    p = Data.GetData.potions()
    p.append(potion)
    Data.PassData.potions(p)
    '''

    '''
    new_amulet = SimpleMagicAmulet()
    a = Data.GetData.artefacts()
    print(new_amulet.mana)

    a.append(new_amulet)

    Data.PassData.artefacts(a)
    '''

    # Battlewar.Battle(hero, 'First_adventure')

    Data.PassData.main_hero(hero)


if __name__ == '__main__':
    main()
