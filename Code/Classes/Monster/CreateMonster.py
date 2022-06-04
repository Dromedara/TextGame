from Code.Classes.Monster import MonsterLinks


class Creator:
    def __init__(self):
        pass

    @staticmethod
    def create_monster(key, lvl):
        """Create monster with its lvl and name of it

        :param key: name of a monster
        :param lvl: lvl o a monster
        :return: created monster
        """
        monster = MonsterLinks.monsters_creator_dict[key](lvl)

        return monster
