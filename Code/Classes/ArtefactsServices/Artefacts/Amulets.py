from Code.Classes.ArtefactsServices.Artefacts import Artefact
import Code.Subfunctions.HelperFunc as HelperFunc


class SimpleMagicAmulet(Artefact):

    passive_simple_magic_amulet = ['simple_magic_baff']

    def __init__(self, _id=0, _rarity=1, mana=0, **kwargs):
        super().__init__()
        self.id = _id
        self.rarity = _rarity
        self.key = 'simple_amulet'
        self.mana += HelperFunc.ForArtefacts.check_input_data(mana, -(self.rarity * 3), -self.rarity)
        self.passive_skills.extend(self.passive_simple_magic_amulet)

    @staticmethod
    def simple_magic_baff(hero, monster):
        hero.hp *= 1.2
        return hero, monster


class SuperMagicAmulet(SimpleMagicAmulet):

    passive_super_magic_amulet = ['super_magic_baff']
    active_super_magic_amulet = ['super_magic_attack']

    def __init__(self, _id=0, _rarity=1, mana=0, **kwargs):
        super().__init__()
        self.id = _id
        self.rarity = _rarity
        self.key = 'super_amulet'
        self.mana += HelperFunc.ForArtefacts.check_input_data(mana, -(self.rarity * 4), -(self.rarity * 2))
        self.passive_skills.extend(self.passive_super_magic_amulet)
        self.active_skills.extend(self.active_super_magic_amulet)

    @staticmethod
    def super_magic_baff(hero, monster):
        hero.hp *= 1.5
        return hero, monster

    @staticmethod
    def super_magic_attack(hero, monster):
        monster.hp -= (hero.magic_attack - 0.3 * monster.defence)
        monster.defence = HelperFunc.ForBattle.battle_params_change(monster.defence, 0.5 * hero.attack)
        return hero, monster