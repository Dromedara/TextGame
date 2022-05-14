from COde_1.BasicFuncs.Start.RecreateEverything import RecreateAdventurer
from COde_1.BasicFuncs.Start.RecreateEverything import RecreateEquipment


def start_it():
    hero = RecreateAdventurer.get_hero(False)
    RecreateEquipment.get_equip(False)

    return hero
