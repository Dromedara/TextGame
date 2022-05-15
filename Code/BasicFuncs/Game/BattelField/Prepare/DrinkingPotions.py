from Code.BasicFuncs.Game.BattelField.BattleSubFuncs import BattleChecker
from Code.BasicFuncs.Game.HelperFuncs.Errors import NotPossibleToUse


class Drinking:

    def __init__(self):
        pass

    @staticmethod
    def drink_potion(hero, potion):

        old_hero = hero
        try:

            hero.attack = BattleChecker.params_change(hero.attack, potion.attack)

            hero.defence = BattleChecker.params_change(hero.defence, potion.defence)

            hero.hp = BattleChecker.hp_change(hero.hp, potion.hp)

            hero.mana = BattleChecker.params_change(hero.mana, potion.mana)

            hero.magic_attack = BattleChecker.params_change(hero.magic_attack, potion.magic_attack)

            hero.tiks = BattleChecker.tiks_add(hero.tiks, potion.key)

            hero.tiks[potion.key] = potion.tik

            return hero

        except NotPossibleToUse:
            return old_hero