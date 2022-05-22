from Code.BasicFuncs.Game.Guild import GuildLinks
from Code.BasicFuncs.Game.BattelField.BattleRunner import Battle


def change_block(choice):
    flag = False

    for name in GuildLinks.adventures_names:
        if flag:
            GuildLinks.adventures_dict[name].blocked = False
            break

        if name == choice:
            flag = True


def change_state(adventurer, choice):

    adventurer.gold += GuildLinks.adventures_dict[choice].gold
    adventurer.exp += GuildLinks.adventures_dict[choice].exp

    GuildLinks.adventures_dict[choice].done = True


def choose_adventure(adventure):

    while True:

        for i in GuildLinks.adventures_dict.values():
            print(f'{i.key}', end='')
            if i.blocked:
                print('[blocked]', end='')
            if i.done:
                print('[done]', end='')
            print()

        choice = input()
        if choice != '':
            adventurer, win = Battle(adventure, choice)
            if win:
                if not GuildLinks.adventures_dict[choice].done:
                    change_state(adventurer, choice)
                    change_block(choice)




