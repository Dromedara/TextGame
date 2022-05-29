from Code.BasicFuncs.Game.Shop.Buying import buy_smth
from Code.BasicFuncs.Game.Warehouse import EquippingRunner
from Code.BasicFuncs.Game.Guild import GuildHall


def play_it():

    while True:

        print('buy equip battle end')
        choice = input()

        if choice == 'buy':
            buy_smth()
        elif choice == 'equip':
            EquippingRunner.run_it()
        elif choice == 'battle':
            GuildHall.choose_adventure()
        else:
            break

