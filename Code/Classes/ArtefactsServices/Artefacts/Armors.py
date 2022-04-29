from Code.Classes.ArtefactsServices.Artefacts import Artefact
import Code.Subfunctions.HelperFunc as HelperFunc


class SimpleIronArmor(Artefact):

    def __init__(self, _id=0, _rarity=1, defence=0, **kwargs):
        super().__init__()
        self.id = _id
        self.rarity = _rarity
        self.key = 'simple_iron_armor'
        self.defence += HelperFunc.ForArtefacts.check_input_data(defence, self.rarity, self.rarity * 3)


class CharmedIronArmor(SimpleIronArmor):

    passive_charmed_iron_armor = ['simple_passive_attack']

    def __init__(self, _id=0, _rarity=1, defence=0, mana=0, magic_atack=0, **kwargs):
        super().__init__()
        self.id = _id
        self.rarity = _rarity
        self.key = 'charmed_iron_armor'
        self.defence += HelperFunc.ForArtefacts.check_input_data(defence, self.rarity * 5, self.rarity * 10)

        self.mana += HelperFunc.ForArtefacts.check_input_data(mana, -(self.rarity * 2), -self.rarity)
        self.magic_attack += HelperFunc.ForArtefacts.check_input_data(magic_atack, self.rarity * 2, self.rarity * 3)
        self.passive_skills.extend(self.passive_charmed_iron_armor)

    @staticmethod
    def simple_passive_attack(hero, monster):
        monster.hp -= (hero.attack - 0.9 * monster.defence)
        return hero, monster
