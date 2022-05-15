from Code.BasicFuncs.Game.Shop.Buying import buy_smth
from Code.BasicFuncs.Finish.FinishGame import finish_it


def play_it(hero):

    while True:

        print('buy battle end')
        choice = input()

        if choice == 'buy':
            hero = buy_smth(hero)
        elif choice == 'battle':
            pass
        else:
            finish_it(hero)
            break

    return hero

