import Code.BasicFuncs.Finish.SaveData.SaveData as SaveData


def finish_it(hero):

    print(hero.lvl)
    SaveData.save_hero(hero=hero)
    SaveData.save_artefacts()
    SaveData.save_potions()
