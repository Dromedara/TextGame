import Code.Classes.ArtefactsServices.Artefacts as Artefacts

artefacts_dict = {
        'simple_iron_armor': Artefacts.Armors.SimpleIronArmor,
        'charmed_iron_armor': Artefacts.Armors.CharmedIronArmor,
        'simple_amulet': Artefacts.Amulets.SimpleMagicAmulet,
        'super_amulet': Artefacts.Amulets.SuperMagicAmulet,
        'simple_sword': Artefacts.Swords.SimpleSword,
        'charmed_sword': Artefacts.Swords.CharmedSword
    }


class Creator:

    def __init__(self):
        pass

    @staticmethod
    def create_artefact(key, id, rarity, attack, defence, hp, mana, magic_attack):

        global artefacts_dict

        artefact = artefacts_dict[key](_id=id,
                                       _rarity=rarity,
                                       attack=attack,
                                       defence=defence,
                                       hp=hp,
                                       mana=mana,
                                       magic_attack=magic_attack)

        return artefact
