from Code.BasicFuncs.Game.BattelField import BattleFuncs
from Code.BasicFuncs.Game.HelperFuncs.Errors import NoHP


def Battle(adventurer, adventure):

    hero = BattleFuncs.Preparing.prepare_hero(adventurer)

    monster = BattleFuncs.Preparing.prepare_monster(adventure)

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
