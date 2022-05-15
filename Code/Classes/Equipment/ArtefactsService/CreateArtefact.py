import Code.Classes.Equipment.ArtefactsService.ArtefactsLinks as ArtefactsLinks


class ArtefactCreator:

    @staticmethod
    def create_artefact(key, _id=-1, rarity=1, attack=0, defence=0, hp=0, mana=0, magic_attack=0):

        if _id == -1:
            ArtefactsLinks.id_counter += 1
            _id = ArtefactsLinks.id_counter

        artefact = ArtefactsLinks.creator_dict[key](_id=_id,
                                                    _rarity=rarity,
                                                    attack=attack,
                                                    defence=defence,
                                                    hp=hp,
                                                    mana=mana,
                                                    magic_attack=magic_attack)

        return artefact
