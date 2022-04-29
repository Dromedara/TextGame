from Code.Classes.ArtefactsServices.Artefacts import Artefact
import Code.Subfunctions.HelperFunc as HelperFunc


class SimpleSword(Artefact):

    active_simple_sword_skills = ['straight_sword_attack']

    def __init__(self, _id=0, _rarity=1, attack=0, **kwargs):
        super().__init__()
        self.id = _id
        self.rarity = _rarity
        self.key = 'simple_sword'
        self.attack += HelperFunc.ForArtefacts.check_input_data(attack, self.rarity, self.rarity * 2)
        self.active_skills.extend(self.active_simple_sword_skills)

    @staticmethod
    def straight_sword_attack(hero, monster):
        monster.hp -= (hero.attack - 0.5 * monster.defence)
        monster.defence = HelperFunc.ForBattle.battle_params_change(monster.defence, 0.3 * hero.attack)
        hero.hp -= 1
        return hero, monster


class CharmedSword(SimpleSword):

    active_charmed_sword_skills = ['forced_sword_attack', 'charmed_sword_attack']

    def __init__(self, _id=0, _rarity=1, attack=0, magic_attack=0, **kwargs):
        super().__init__()
        self.id = _id
        self.rarity = _rarity
        self.key = 'charmed_sword'
        self.attack += HelperFunc.ForArtefacts.check_input_data(attack, self.rarity * 2, self.rarity * 4)
        self.magic_attack += HelperFunc.ForArtefacts.check_input_data(magic_attack, self.rarity, self.rarity * 2)
        self.active_skills.extend(self.active_charmed_sword_skills)

    @staticmethod
    def forced_sword_attack(hero, monster):
        monster.hp -= (hero.attack - 0.3 * monster.defence)
        monster.defence = HelperFunc.ForBattle.battle_params_change(monster.defence, 0.5 * hero.attack)
        hero.hp -= 1.2
        return hero, monster

    @staticmethod
    def charmed_sword_attack(hero, monster):
        monster.hp -= (hero.attack - 0.2 * monster.defence)
        monster.defence = HelperFunc.ForBattle.battle_params_change(monster.defence, 0.3 * hero.attack)

        if hero.mana == 0:
            hero.hp -= 2
        hero.mana = HelperFunc.ForBattle.battle_params_change(hero.mana, 0.5)
        return hero, monster
