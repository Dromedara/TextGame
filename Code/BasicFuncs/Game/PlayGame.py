from Code.BasicFuncs.Game.Shop.Buying import buy_smth
from Code.BasicFuncs.Finish.FinishGame import finish_it
from Code.BasicFuncs.Game.Warehouse import EquippingRunner
from Code.BasicFuncs.Game.Guild import GuildHall


def play_it(hero):

    while True:

        print('buy equip battle end')
        choice = input()

        if choice == 'buy':
            hero = buy_smth(hero)
        elif choice == 'equip':
            EquippingRunner.run_it()
        elif choice == 'battle':
            GuildHall.choose_adventure(hero)
        else:
            finish_it(hero)
            break

    return hero

