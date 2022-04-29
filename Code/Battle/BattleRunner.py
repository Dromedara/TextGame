import Code.Battle.BattleFuncs as BattleFuncs
import Code.Battle.BattleSubFuncs as BattleSubFuncs

import random


def Battle(adventurer, adventure):

    hero = BattleFuncs.Prepearing.prepare_hero(adventurer)

    monster = BattleFuncs.Prepearing.prepare_monster(adventure)

    potions = BattleFuncs.Prepearing.prepare_potions()

    hero.remember_params()

    while hero.hp > 0 and monster.hp > 0:

        # hero
        BattleSubFuncs.Other.show(hero)




