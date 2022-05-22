import Code.BasicFuncs.DataOperations.SaveData as SaveData


def save_main_inventory():
    SaveData.save_artefacts()
    SaveData.save_armors()
    SaveData.save_potions()
    SaveData.save_id()


def save_battle_inventory():
    SaveData.save_battle_armors()
    SaveData.save_battle_artefacts()
    SaveData.save_battle_potions()


def save_hero(hero):
    SaveData.save_hero(hero=hero)


def save_adventures():
    SaveData.save_adventures()


def finish_it(hero):
    save_hero(hero)
    save_main_inventory()
    save_battle_inventory()
    save_adventures()

