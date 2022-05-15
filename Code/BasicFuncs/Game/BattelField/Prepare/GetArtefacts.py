from Code.BasicFuncs.Game.BattelField.BattleSubFuncs import BattleChecker
from Code.BasicFuncs.Game.HelperFuncs.Errors import NotPossibleToUse


class Getting:

    def __init__(self):
        pass

    @staticmethod
    def get_equipment(hero, equipment):

        old_hero = hero

        try:
            hero.attack = BattleChecker.params_change(hero.attack, equipment.attack)

            hero.defence = BattleChecker.params_change(hero.defence, equipment.defence)

            hero.hp = BattleChecker.hp_change(hero.hp, equipment.hp)

            hero.mana = BattleChecker.params_change(hero.mana, equipment.mana)

            hero.magic_attack = BattleChecker.params_change(hero.magic_attack, equipment.magic_attack)

            hero.hero_active_skills['artefacts'].extend(equipment.active_skills)

            hero.hero_passive_skills['artefacts'].extend(equipment.passive_skills)

            return hero

        except NotPossibleToUse:
            return old_hero