import Code.Data.InOutData as Data
import Code.Battle.BattleProcess as Battlewar
from Code.Classes.Equipment.Artefacts import SimpleMagicAmulet


def main():

    hero = Data.GetData.main_hero()

    print(hero.name)

    new_amulet = SimpleMagicAmulet()
    a = Data.GetData.artefacts()
    print(new_amulet.mana)

    a.append(new_amulet)

    Data.PassData.artefacts(a)

    # Battlewar.Battle(hero, 'First_adventure')

    Data.PassData.main_hero(hero)


if __name__ == '__main__':
    main()
