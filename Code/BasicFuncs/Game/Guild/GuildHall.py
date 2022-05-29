from Code.BasicFuncs.Game.Guild import GuildLinks
from Code.BasicFuncs.Game.BattelField.BattleRunner import Battle

from Code.Classes.MainHero.Savior import ReadHero


def change_block(choice):
    flag = False

    for name in GuildLinks.adventures_names:
        if flag:
            GuildLinks.adventures_dict[name].blocked = False
            break

        if name == choice:
            flag = True


def change_state(choice):
    adventurer = ReadHero.read_it()
    adventurer.gold += GuildLinks.adventures_dict[choice].gold
    adventurer.exp += GuildLinks.adventures_dict[choice].exp
    ReadHero.save_it()

    GuildLinks.adventures_dict[choice].done = True


def choose_adventure():

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
            if Battle(choice):
                change_state(choice)
                change_block(choice)
        else:
            break

