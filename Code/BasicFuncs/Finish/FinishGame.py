import Code.BasicFuncs.DataOperations.SaveData as SaveData


def finish_it(hero):

    SaveData.save_hero(hero=hero)
    SaveData.save_artefacts()
    SaveData.save_armors()
    SaveData.save_potions()
    SaveData.save_id()
