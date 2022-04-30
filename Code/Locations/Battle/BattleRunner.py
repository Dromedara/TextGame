import Code.Locations.Battle.BattleFuncs as BattleFuncs
import Code.Locations.Battle.BattleSubFuncs as BattleSubFuncs

curr_artefacts = {}

curr_potions = {}


def Battle(adventurer, adventure):


    global curr_potions
    global curr_artefacts

    hero = BattleFuncs.Prepearing.prepare_hero(adventurer)

    monster = BattleFuncs.Prepearing.prepare_monster(adventure)

    hero.remember_params()

    while hero.hp > 0 and monster.hp > 0:

        # hero

        BattleFuncs.PotionsActions.run_it(hero)

        BattleSubFuncs.Show.show_potions(curr_potions)


        # выпить зелье - проверка
        # пассивки - проверк
        # баффы - проверка
        # выбор атаки - проверка



