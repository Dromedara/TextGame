import COde_1.Classes.Equipment.PotionsService.PotionsLinks as PotionsLinks


class PotionsCreator:

    @staticmethod
    def create_potion(key, _id=-1, rarity=1, tik=0, attack=0, defence=0, hp=0, mana=0, magic_attack=0):

        if _id == -1:
            PotionsLinks.id_counter += 1
            _id = PotionsLinks.id_counter

        potion = PotionsLinks.potions_creator[key](_rarity=rarity,
                                                   _id=_id,
                                                   _tik=tik,
                                                   attack=attack,
                                                   defence=defence,
                                                   hp=hp,
                                                   mana=mana,
                                                   magic_attack=magic_attack)

        return potion
