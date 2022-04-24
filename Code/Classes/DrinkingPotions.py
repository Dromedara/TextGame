import Code.Checking.Errors as Errors
import Code.Checking.SOS as SOS


class Drinking:

    def __init__(self):
        pass

    @staticmethod
    def drink_it(hero, potion):
        try:
            hero.attack = hero.checker.possible_change(hero.attack, potion.attack)
        except Errors.ImpossibleChange:
            SOS.SOSMessages.impossible_to_use()

        try:
            hero.defence = hero.checker.possible_change(hero.defence, potion.defence)
        except Errors.ImpossibleChange:
            SOS.SOSMessages.impossible_to_use()

        try:
            hero.hp = hero.checker.possible_change(hero.hp, potion.hp)
        except Errors.ImpossibleChange:
            SOS.SOSMessages.impossible_to_use()

        try:
            hero.mana = hero.checker.possible_change(hero.mana, potion.mana)
        except Errors.ImpossibleChange:
            SOS.SOSMessages.impossible_to_use()

        try:
            hero.magic_attack = hero.checker.possible_change(hero.magic_attack, potion.magic_attack)
        except Errors.ImpossibleChange:
            SOS.SOSMessages.impossible_to_use()

        return hero
