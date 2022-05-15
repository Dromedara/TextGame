from Code.Classes.Monster import MonsterLinks


class Creator:
    def __init__(self):
        pass

    @staticmethod
    def create_monster(key, lvl):

        monster = MonsterLinks.monsters_creator_dict[key](lvl)

        return monster
