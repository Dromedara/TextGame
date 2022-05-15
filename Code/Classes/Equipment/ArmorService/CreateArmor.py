import Code.Classes.Equipment.ArmorService.ArmorLinks as ArmorLinks


class ArmorCreator:

    @staticmethod
    def create_armor(key, _id=-1, rarity=1, attack=0, defence=0, hp=0, mana=0, magic_attack=0):

        if _id == -1:
            ArmorLinks.id_counter += 1
            _id = ArmorLinks.id_counter

        armor = ArmorLinks.creator_dict[key](_id=_id,
                                             _rarity=rarity,
                                             attack=attack,
                                             defence=defence,
                                             hp=hp,
                                             mana=mana,
                                             magic_attack=magic_attack)

        return armor
