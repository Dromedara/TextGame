from Code.BasicFuncs.Game.Warehouse.Equipping import Choose


def run_it():

    while True:
        print(':::')

        choice = input()
        if choice == 'artefacts':
            Choose.choose_artefacts()
        elif choice == 'potions':
            Choose.choose_potions()
        elif choice == 'armor':
            Choose.choose_armors()
        else:
            break
