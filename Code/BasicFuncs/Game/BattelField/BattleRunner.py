from Code.BasicFuncs.Game.BattelField import BattleFuncs
from Code.BasicFuncs.Game.HelperFuncs.Errors import NoHP
from Code.BasicFuncs.Game.HelperFuncs.Errors import MonsterDied
from Code.BasicFuncs.Game.BattelField.BattleSubFuncs import Show
from Code.BasicFuncs.Game.BattelField.StartBattle import Preparing
from Code.BasicFuncs.Game.BattelField.EndBattle import Ending

from Code.Classes.MainHero.Savior import ReadHero


def Battle(adventure):

    adventurer = ReadHero.read_it()

    hero = Preparing.prepare_hero(adventurer)
    monster = Preparing.prepare_monster(adventure)

    print(monster.key)

    try:
        while True:

            hero.remember_params()

            Show.show_hero(hero)
            Show.show_monster(monster)

            hero, monster = BattleFuncs.PassiveActions.run_it(hero, monster)
            
            hero = BattleFuncs.PotionsActions.run_it(hero)

            Show.show_hero(hero)
            Show.show_monster(monster)

            hero, monster = BattleFuncs.ActiveActions.run_it(hero, monster)

            Show.show_hero(hero)
            Show.show_monster(monster)

            hero, monster = BattleFuncs.MonsterActions.run_it(hero, monster)

            Show.show_hero(hero)
            Show.show_monster(monster)

    except MonsterDied:
        return Ending.end_game(monster, True)
    except NoHP:
        return Ending.end_game(monster, False)


