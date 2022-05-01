from Code.StartAndFinish.StartGame import Starter
from Code.StartAndFinish.FinishGame import Finisher
from Code.Locations.Shop import Buying
from Code.Locations.Warehouse import Equipping
from Code.Locations.Battle import BattleRunner


def main():

    #hero = Starter.lets_start_new()
    hero = Starter.lets_start_again()

    print(hero)

    hero = Buying.buy_smth(hero=hero)

    print('CHOOSE')
    BattleRunner.curr_artefacts = Equipping.Choose.choose_artifacts()

    BattleRunner.curr_potions = Equipping.Choose.choose_potions()

    print('BATTLE')

    BattleRunner.Battle(hero, 'FirstAdventure')

    Finisher.lets_finish(hero=hero)


if __name__ == '__main__':
    main()
