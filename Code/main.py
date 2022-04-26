import Code.SavingData.Characters as Data
import Code.Battle.BattleProcess as Battlewar


def main():

    hero = Data.GetData.main_hero()

    print(hero.name)

    Battlewar.Battle(hero, 'First_adventure')

    Data.PassData.main_hero(hero)


if __name__ == '__main__':
    main()
