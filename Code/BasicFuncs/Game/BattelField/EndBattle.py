from Code.BasicFuncs.Game.Warehouse.Inventory import Battle
from Code.BasicFuncs.Game.Warehouse.Inventory.Main import main_inventory


class Ending:

    @staticmethod
    def reequip():
        main_inventory.del_potions_done()
        Battle.done_potions = []

    @staticmethod
    def win(hero, monster):
        print('You win')
        hero.gold += monster.gold
        hero.change_exp(monster.exp)

    @staticmethod
    def loose():
        print('You loose')
        pass
