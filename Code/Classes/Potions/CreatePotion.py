import Code.Classes.Potions.Potions as Potions


dict_of_links = {
            'healing_potion': Potions.HealingPotion,
            'boosting_potion': Potions.BoostingPotion,
            'protecting_potion': Potions.ProtectingPotion
        }


class Creator:

    def __init__(self):
        pass

    @staticmethod
    def create_potion(line):

        global dict_of_links

        vals = list(map(str, line.split()))

        potion = dict_of_links[vals[0]](_rarity=int(vals[1]), attack=float(vals[2]), defence=float(vals[3]),
                               hp=float(vals[4]), mana=float(vals[5]), magic_attack=float(vals[6]))

        return potion
