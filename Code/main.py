from Code.StartAndFinish.StartGame import Starter
from Code.StartAndFinish.FinishGame import Finisher
from Code.Locations.Shop import Buying
from Code.Locations.Warehouse import Equipping


def main():

    hero, Equipping.artefacts_list, Equipping.potions_list = Starter.lets_start_new()
    # hero, artefacts, potions = Starter.lets_start_again()

    hero.name = 'Alan'

    hero, artefacts, potions = Buying.buy_smth(hero=hero)

    curr_artefacts = Equipping.Choose.choose_artifacts(artefacts=Equipping.artefacts_list)

    print(curr_artefacts)

    # curr_potios = Choose.c


    Finisher.lets_finish(hero=hero, artefacts=Equipping.artefacts_list, potions=Equipping.potions_list)


if __name__ == '__main__':
    main()
