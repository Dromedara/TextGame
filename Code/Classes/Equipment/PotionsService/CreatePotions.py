import Code.Classes.Equipment.PotionsService.PotionsLinks as PotionsLinks
import Code.Classes.Equipment.IDCounter as ID


class PotionsCreator:

    @staticmethod
    def create_potion(key, _id=-1, rarity=1, tik=0, attack=0, defence=0, hp=0, mana=0, magic_attack=0):
        if _id == -1:
            _id = ID.id_creator.create_new()

        potion = PotionsLinks.potions_creator[key](_rarity=rarity,
                                                   _id=_id,
                                                   _tik=tik,
                                                   attack=attack,
                                                   defence=defence,
                                                   hp=hp,
                                                   mana=mana,
                                                   magic_attack=magic_attack)

        return potion
