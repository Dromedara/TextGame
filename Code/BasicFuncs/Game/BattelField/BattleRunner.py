from Code.BasicFuncs.Game.BattelField import BattleFuncs
from Code.BasicFuncs.Game.HelperFuncs.Errors import NoHP
from Code.BasicFuncs.Game.HelperFuncs.Errors import MonsterDied
from Code.BasicFuncs.Game.BattelField.BattleSubFuncs import Show
import Code.BasicFuncs.Game.BattelField.EndBattle


def Battle(adventurer, adventure):

    hero = BattleFuncs.Preparing.prepare_hero(adventurer)
    monster = BattleFuncs.Preparing.prepare_monster(adventure)

    print(monster.key)

    try:
        while True:

            hero.remember_params()
            Show.show_hero(hero)

            hero, monster = BattleFuncs.PassiveActions.run_it(hero, monster)
            
            hero = BattleFuncs.PotionsActions.run_it(hero)
            Show.show_hero(hero)

            hero, monster = BattleFuncs.ActiveActions.run_it(hero, monster)

            hero, monster = BattleFuncs.MonsterActions.run_it(hero, monster)

            Show.show_hero(hero)
            print(f'MONSTER: {monster.hp}')

    except NoHP:
        print('You died')

    except MonsterDied:
        print('you WIN')

