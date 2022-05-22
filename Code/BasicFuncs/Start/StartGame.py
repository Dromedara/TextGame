from Code.BasicFuncs.Start.RecreateEverything import RecreateAdventurer
from Code.BasicFuncs.Start.RecreateEverything import RecreateEquipment
from Code.BasicFuncs.DataOperations.GetData import adventure_creator


def start_it(first_activation=True):
    hero = RecreateAdventurer.get_hero(first_activation=first_activation)
    RecreateEquipment.get_equip(first_activation=first_activation)

    return hero
