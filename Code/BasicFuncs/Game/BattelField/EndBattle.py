from Code.BasicFuncs.Game.Warehouse.Inventory import Battle
from Code.BasicFuncs.Game.Warehouse.Inventory.Main import main_inventory
from Code.Classes.MainHero.Savior import ReadHero


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

        ReadHero.save_it()

        return

    @staticmethod
    def loose():
        print('You loose')

    @staticmethod
    def end_game(monster, win):
        Ending.reequip()
        adventurer = ReadHero.read_it()

        if win:
            Ending.win(adventurer, monster)
            return True
        else:
            Ending.loose()
            return False



