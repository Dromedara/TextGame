from Code.BasicFuncs.Game.BattelField.BattleSubFuncs import BattleChecker
from Code.BasicFuncs.Game.HelperFuncs.Errors import NotPossibleToUse


class Drinking:

    def __init__(self):
        pass

    @staticmethod
    def drink_potion(hero, potion):

        old_hero = hero

        try:

            hero.attack = BattleChecker.use_changes(hero.attack, -potion.attack)

            hero.defence = BattleChecker.use_changes(hero.defence, -potion.defence)

            hero.hp = BattleChecker.hp_change(hero.hp, -potion.hp)

            hero.mana = BattleChecker.use_changes(hero.mana, -potion.mana)

            hero.magic_attack = BattleChecker.use_changes(hero.magic_attack, -potion.magic_attack)

            hero.tiks = BattleChecker.tiks_add(hero.tiks, -potion.key)

            hero.tiks[potion.key] = potion.tik

            return hero

        except NotPossibleToUse:
            return old_hero
