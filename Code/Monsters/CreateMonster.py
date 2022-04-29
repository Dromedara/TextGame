import Code.Monsters.Monsters as Monsters

monsters = {
            'Chupakabra': Monsters.Chupakabra
        }


class Creator:
    def __init__(self):
        pass

    @staticmethod
    def create_monster(key, lvl):
        global monsters

        monster = monsters[key](lvl)

        return monster
