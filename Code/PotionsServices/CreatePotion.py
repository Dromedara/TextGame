import Code.PotionsServices.Potions as Potions


potions_dict = {
            'healing_potion': Potions.HealingPotion,
            'boosting_potion': Potions.BoostingPotion,
            'protecting_potion': Potions.ProtectingPotion
        }


class Creator:

    def __init__(self):
        pass

    @staticmethod
    def create_potion(key, rarity=1, tik=0, attack=0, defence=0, hp=0, mana=0, magic_attack=0):
        global potions_dict

        potion = potions_dict[key](_rarity=rarity,
                                   _tik=tik,
                                   attack=attack,
                                   defence=defence,
                                   hp=hp,
                                   mana=mana,
                                   magic_attack=magic_attack)

        return potion
