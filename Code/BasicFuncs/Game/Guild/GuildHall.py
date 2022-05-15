from Code.BasicFuncs.Game.Guild import GuildLinks
from Code.BasicFuncs.Game.BattelField.BattleRunner import Battle


def choose_adventure(hero):

    print(GuildLinks.adventures_list)

    choice = input()

    Battle(hero, choice)


