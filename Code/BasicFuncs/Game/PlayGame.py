from Code.BasicFuncs.Game.Shop.Buying import buy_smth


def play_it(hero):

    while True:

        print('buy battle')
        choice = input()

        if choice == 'buy':
            hero = buy_smth(hero)
        elif choice == 'battle':
            pass
        else:
            break

    return hero

