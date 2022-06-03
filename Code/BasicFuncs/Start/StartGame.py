from Code.BasicFuncs.Start.RecreateEverything import RecreateEquipment
from Code.BasicFuncs.DataOperations.GetData import adventure_creator
from Code.BasicFuncs.Game.Shop import Sellers
from Code.BasicFuncs.Game.Shop import CreateStuff


def start_it(first_activation=True):
    RecreateEquipment.get_equip(first_activation=first_activation)

    adventure_creator()

    Sellers.selling_artefacts, Sellers.selling_armors, Sellers.selling_potions = CreateStuff.start_shop()

