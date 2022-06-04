from Code.BasicFuncs.Game.BattelField.BattleSubFuncs import BattleChecker
from Code.BasicFuncs.Game.HelperFuncs.Errors import NotPossibleToUse
from Code.BasicFuncs.Game.Warehouse.Inventory import Battle


class Drinking:

    def __init__(self):
        pass

    @staticmethod
    def drink_potion(hero, potion_id):

        print(Battle.battle_inventory.curr_potions)

        potion = Battle.battle_inventory.curr_potions[int(potion_id)]

        old_hero = hero

        try:

            hero.attack = BattleChecker.use_changes(hero.attack, potion.attack)

            hero.defence = BattleChecker.use_changes(hero.defence, potion.defence)

            hero.hp = BattleChecker.params_change(hero.hp, potion.hp, hero.param_savior['hp'][0])

            hero.mana = BattleChecker.use_changes(hero.mana, potion.mana)

            hero.magic_attack = BattleChecker.use_changes(hero.magic_attack, potion.magic_attack)

            hero.tiks = BattleChecker.tiks_add(hero.tiks, potion.key)

            hero.tiks[potion.key] = potion.tik

            print(f'{potion.key} was activated!')

            return hero, True

        except NotPossibleToUse:
            return old_hero, False
