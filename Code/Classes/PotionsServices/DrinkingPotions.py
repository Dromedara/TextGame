import Code.Subfunctions.Errors as Errors
import Code.Subfunctions.Messages.SOS as SOS
from Code.Classes.PotionsServices.PotionsSubFuncs import Checker as PotionsChecker
from Code.Classes.MainCharacter.AdventurerSubFuncs import Checker as AdventurerChecker


class Drinking:

    def __init__(self):
        pass

    @staticmethod
    def drink_potion(hero, potion):
        try:
            hero.attack = AdventurerChecker.possible_change(hero.attack, potion.attack)
        except Errors.ImpossibleChange:
            SOS.SOSMessages.impossible_to_use()

        try:
            hero.defence = AdventurerChecker.possible_change(hero.defence, potion.defence)
        except Errors.ImpossibleChange:
            SOS.SOSMessages.impossible_to_use()

        try:
            hero.hp = AdventurerChecker.possible_change(hero.hp, potion.hp)
        except Errors.ImpossibleChange:
            SOS.SOSMessages.impossible_to_use()

        try:
            hero.mana = AdventurerChecker.possible_change(hero.mana, potion.mana)
        except Errors.ImpossibleChange:
            SOS.SOSMessages.impossible_to_use()

        try:
            hero.magic_attack = AdventurerChecker.possible_change(hero.magic_attack, potion.magic_attack)
        except Errors.ImpossibleChange:
            SOS.SOSMessages.impossible_to_use()

        hero.tiks = PotionsChecker.tiks_add(hero.tiks, potion.key)
        hero.tiks[potion.key] = potion.tik

        return hero
