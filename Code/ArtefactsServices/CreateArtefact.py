import Code.ArtefactsServices.Artefact


artefacts_dict = {
        'simple_iron_armor': Code.ArtefactsServices.Artefact.SimpleIronArmor,
        'charmed_iron_armor': Code.ArtefactsServices.Artefact.CharmedIronArmor,
        'simple_amulet': Code.ArtefactsServices.Artefact.SimpleMagicAmulet,
        'super_amulet': Code.ArtefactsServices.Artefact.SuperMagicAmulet,
        'simple_sword': Code.ArtefactsServices.Artefact.SimpleSword,
        'charmed_sword': Code.ArtefactsServices.Artefact.CharmedSword
    }


class Creator:

    def __init__(self):
        pass

    @staticmethod
    def create_artefact(key, id=0, rarity=1, attack=0, defence=0, hp=0, mana=0, magic_attack=0):

        global artefacts_dict

        artefact = artefacts_dict[key](_id=id,
                                       _rarity=rarity,
                                       attack=attack,
                                       defence=defence,
                                       hp=hp,
                                       mana=mana,
                                       magic_attack=magic_attack)

        return artefact
