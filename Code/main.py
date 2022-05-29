import Code.BasicFuncs.Start.StartGame as StartGame
import Code.BasicFuncs.Game.PlayGame as PlayGame
import Code.BasicFuncs.Finish.FinishGame as FinishGame

from Code.BasicFuncs.Game.Warehouse.Inventory.Main import main_inventory


def main():
    StartGame.start_it(first_activation=False)
    print(main_inventory.get_armors())
    PlayGame.play_it()
    FinishGame.finish_it()


if __name__ == '__main__':
    main()
