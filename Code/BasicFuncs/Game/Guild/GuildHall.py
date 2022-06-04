from Code.BasicFuncs.Game.Guild import GuildLinks

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
    ReadHero.save_it(hero=adventurer)

    GuildLinks.adventures_dict[choice].done = True


def all_adventures():
    l = list()
    o = list()
    k = ""
    for i in GuildLinks.adventures_dict.values():
        k = str(i.key)
        o.append(k)
        k = ""
        if i.blocked:
            k = "[blocked]"
        elif i.done:
            k = "[done]"
        o.append(k)
        l.append(o)
        o = list()
        k = ""
    return l




