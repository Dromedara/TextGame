import Code.Classes.ArtefactsServices.Artefacts.Amulets
import Code.Classes.ArtefactsServices.Artefacts.Swords
import Code.Classes.ArtefactsServices.Artefacts.Armors

artefacts_dict = {
        'simple_iron_armor': Code.Classes.ArtefactsServices.Artefacts.Armors.SimpleIronArmor,
        'charmed_iron_armor': Code.Classes.ArtefactsServices.Artefacts.Armors.CharmedIronArmor,
        'simple_amulet': Code.Classes.ArtefactsServices.Artefacts.Amulets.SimpleMagicAmulet,
        'super_amulet': Code.Classes.ArtefactsServices.Artefacts.Amulets.SuperMagicAmulet,
        'simple_sword': Code.Classes.ArtefactsServices.Artefacts.Swords.SimpleSword,
        'charmed_sword': Code.Classes.ArtefactsServices.Artefacts.Swords.CharmedSword
    }


_id_counter = 0


class Creator:

    def __init__(self):
        pass

    @staticmethod
    def create_artefact(key, id=-1, rarity=1, attack=0, defence=0, hp=0, mana=0, magic_attack=0):

        global artefacts_dict
        global _id_counter

        if id == -1:
            id = _id_counter
            _id_counter += 1

        artefact = artefacts_dict[key](_id=id,
                                       _rarity=rarity,
                                       attack=attack,
                                       defence=defence,
                                       hp=hp,
                                       mana=mana,
                                       magic_attack=magic_attack)

        return artefact
