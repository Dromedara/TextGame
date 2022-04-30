from Code.Classes.ArtefactsServices.ArtefactsSubFuncs import Checker as ArtefactChecker
from Code.Classes.MainCharacter.AdventurerSubFuncs import Checker as AdventurerChecker
import Code.Subfunctions.Errors as Errors
import Code.Subfunctions.Messages.SOS as SOS
from Code.Subfunctions.Messages.Attention import AttentionMessages


class Wearing:

    def __init__(self):
        pass

    @staticmethod
    def get_equipment(hero, equipment):

        try:
            hero.attack = AdventurerChecker.possible_change(hero.attack, equipment.attack)
        except Errors.ImpossibleChange:
            SOS.SOSMessages.impossible_to_use()

        try:
            hero.defence = AdventurerChecker.possible_change(hero.defence, equipment.defence)
        except Errors.ImpossibleChange:
            SOS.SOSMessages.impossible_to_use()

        try:
            hero.hp = AdventurerChecker.possible_change(hero.hp, equipment.hp)
        except Errors.ImpossibleChange:
            SOS.SOSMessages.impossible_to_use()

        try:
            hero.mana = AdventurerChecker.possible_change(hero.mana, equipment.mana)
        except Errors.ImpossibleChange:
            SOS.SOSMessages.impossible_to_use()

        try:
            hero.magic_attack = AdventurerChecker.possible_change(hero.magic_attack, equipment.magic_attack)
        except Errors.ImpossibleChange:
            SOS.SOSMessages.impossible_to_use()

        hero.hero_active_skills = ArtefactChecker.skills_add(hero.hero_active_skills, equipment.key)
        hero.hero_active_skills[equipment.key].extend(equipment.active_skills)

        hero.hero_passive_skills = ArtefactChecker.skills_add(hero.hero_passive_skills, equipment.key)
        hero.hero_passive_skills[equipment.key].extend(equipment.passive_skills)

        AttentionMessages.successfully_done()

        return hero
