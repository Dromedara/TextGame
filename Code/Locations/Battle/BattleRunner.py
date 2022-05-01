import Code.Locations.Battle.BattleFuncs as BattleFuncs
import Code.Locations.Battle.BattleSubFuncs as BattleSubFuncs
from Code.Subfunctions.Errors import NoHP


curr_artefacts = {}

curr_potions = {}


def Battle(adventurer, adventure):

    hero = BattleFuncs.Prepearing.prepare_hero(adventurer)

    monster = BattleFuncs.Prepearing.prepare_monster(adventure)

    hero.remember_params()

    try:
        while True:

            # hero

            hero.remember_params()

            hero = BattleFuncs.PotionsActions.run_it(hero)

            hero, monster = BattleFuncs.PassiveActions.run_it(hero, monster)

            # баффы - проверка
            # выбор атаки - проверка

    except NoHP:
        print('You died')

