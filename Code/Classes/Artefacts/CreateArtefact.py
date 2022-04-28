import Code.Classes.Artefacts.Artefacts as Artefacts

dict_of_links = {
        'simple_iron_armor': Artefacts.SimpleIronArmor,
        'charmed_iron_armor': Artefacts.CharmedIronArmor,
        'simple_amulet': Artefacts.SimpleMagicAmulet,
        'super_amulet': Artefacts.SuperMagicAmulet,
        'simple_sword': Artefacts.SimpleSword,
        'charmed_sword': Artefacts.CharmedSword
    }


class Creator:

    def __init__(self):
        pass

    @staticmethod
    def create_artefact(line):

        global dict_of_links

        vals = list(map(str, line.split()))

        artefact = dict_of_links[vals[0]](_id=int(vals[1]), _rarity=int(vals[2]), attack=float(vals[3]),
                               defence=float(vals[4]), hp=float(vals[5]), mana=float(vals[6]),
                               magic_attack=float(vals[7]))

        return artefact
