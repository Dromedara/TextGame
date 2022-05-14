import COde_1.Locations.Battle.BattleFuncs as BattleFuncs
import COde_1.Locations.Battle.BattleSubFuncs as BattleSubFuncs
from COde_1.Subfunctions.Errors import NoHP


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
