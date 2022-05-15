from Code.BasicFuncs.Start.RecreateEverything import RecreateAdventurer
from Code.BasicFuncs.Start.RecreateEverything import RecreateEquipment
from Code.BasicFuncs.Start.GetData.Reset import adventure_creator

import Code.Classes.Equipment.IDCounter as ID


def start_it(first_activation=True):
    hero = RecreateAdventurer.get_hero(first_activation=first_activation)
    RecreateEquipment.get_equip(first_activation=first_activation)

    adventure_creator()
    
    print(ID.id_creator.id)

    return hero
