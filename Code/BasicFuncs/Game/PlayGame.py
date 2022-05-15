from Code.BasicFuncs.Game.Shop.Buying import buy_smth
from Code.BasicFuncs.Finish.FinishGame import finish_it
from Code.BasicFuncs.Game.Warehouse import EquippingRunner


def play_it(hero):

    while True:

        print('buy equip battle end')
        choice = input()

        if choice == 'buy':
            hero = buy_smth(hero)
        elif choice == 'equip':
            EquippingRunner.run_it()
        elif choice == 'battle':
            pass
        else:
            finish_it(hero)
            break

    return hero

