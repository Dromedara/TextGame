import Code.Classes.Equipment.ArtefactsService.ArtefactsLinks as ArtefactsLinks
import Code.Classes.Equipment.IDCounter as ID


class ArtefactCreator:

    @staticmethod
    def create_artefact(key, _id=-1, rarity=1, attack=0, defence=0, hp=0, mana=0, magic_attack=0):

        if _id == -1:
            _id = ID.id_creator.create_new()

        artefact = ArtefactsLinks.creator_dict[key](_id=_id,
                                                    _rarity=rarity,
                                                    attack=attack,
                                                    defence=defence,
                                                    hp=hp,
                                                    mana=mana,
                                                    magic_attack=magic_attack)

        return artefact
