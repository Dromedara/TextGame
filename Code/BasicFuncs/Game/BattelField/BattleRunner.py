from Code.BasicFuncs.Game.BattelField import BattleFuncs
from Code.BasicFuncs.Game.HelperFuncs.Errors import NoHP


def Battle(adventurer, adventure):

    hero = BattleFuncs.Preparing.prepare_hero(adventurer)
    monster = BattleFuncs.Preparing.prepare_monster(adventure)

    print(monster.key)

    try:
        while True:

            hero.remember_params()
            print(hero.param_savior)

            hero, monster = BattleFuncs.PassiveActions.run_it(hero, monster)

            hero = BattleFuncs.PotionsActions.run_it(hero)

            # баффы - проверка
            # выбор атаки - проверка

    except NoHP:
        print('You died')
