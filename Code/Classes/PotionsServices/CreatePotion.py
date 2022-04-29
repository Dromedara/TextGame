import Code.Classes.PotionsServices.Potions as Potions


potions_dict = {
            'healing_potion': Potions.HealingPotion,
            'boosting_potion': Potions.BoostingPotion,
            'protecting_potion': Potions.ProtectingPotion
        }


class Creator:

    def __init__(self):
        pass

    @staticmethod
    def create_potion(key, rarity, tik, attack, defence, hp, mana, magic_attack):
        global potions_dict

        potion = potions_dict[key](_rarity=rarity,
                                   _tik=tik,
                                   attack=attack,
                                   defence=defence,
                                   hp=hp,
                                   mana=mana,
                                   magic_attack=magic_attack)

        return potion
