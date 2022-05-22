from Code.BasicFuncs.Game.Warehouse.Inventory import Battle
from Code.BasicFuncs.Game.Warehouse.Inventory.Main import main_inventory


class Ending:

    @staticmethod
    def reequip():
        main_inventory.del_potions_done()
        Battle.done_potions = []

    @staticmethod
    def win(adventurer, monster):
        print('You win')
        adventurer.gold += monster.gold
        adventurer.change_exp(monster.exp)

        return adventurer

    @staticmethod
    def loose(adventurer):
        print('You loose')

    @staticmethod
    def end_game(adventurer, monster, win):
        Ending.reequip()

        if win:
            adventurer = Ending.win(adventurer, monster)
            return adventurer, True
        else:
            Ending.loose(adventurer)
            return adventurer, False



