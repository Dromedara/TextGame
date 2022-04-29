from Code.StartAndFinish.StartGame import Starter
from Code.StartAndFinish.FinishGame import Finisher
import Code.Shop.Buying as Shopping
from Code.MainRepository.Equipping import Choose


def main():

    hero, artefacts, potions = Starter.lets_start_new()
    #hero, artefacts, potions = Starter.lets_start_again()

    hero.name = 'Alan'

    hero, artefacts, potions = Shopping.buy_smth(hero=hero)

    curr_artefacts = Choose.choose_artifacts(artefacts=artefacts)
    #curr_potios =

    Finisher.lets_finish(hero=hero, artefacts=artefacts, potions=potions)


if __name__ == '__main__':
    main()
