from Code.StartAndFinish.StartGame import Starter
from Code.StartAndFinish.FinishGame import Finisher
from Code.Locations.Shop import Buying
from Code.Locations.Warehouse import Equipping
from Code.Locations.Battle import BattleRunner


def main():

    hero, Equipping.artefacts_list, Equipping.potions_list = Starter.lets_start_new()
    # hero, artefacts, potions = Starter.lets_start_again()

    hero, artefacts, potions = Buying.buy_smth(hero=hero)

    BattleRunner.curr_artefacts = Equipping.Choose.choose_artifacts(artefacts=Equipping.artefacts_list)

    BattleRunner.curr_potions = Equipping.Choose.choose_potions(potions=Equipping.potions_list)

    Finisher.lets_finish(hero=hero, artefacts=Equipping.artefacts_list, potions=Equipping.potions_list)


if __name__ == '__main__':
    main()
