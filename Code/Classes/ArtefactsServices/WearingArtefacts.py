import Code.Subfunctions.HelperFunc as HelperFunc
import Code.Subfunctions.Errors as Errors
import Code.Subfunctions.Messages.SOS as SOS
from Code.Subfunctions.Messages.Attention import AttentionMessages


class Wearing:

    def __init__(self):
        pass

    @staticmethod
    def get_equipment(hero, equipment):

        try:
            hero.attack = HelperFunc.ForAdventurerFuncs.possible_change(hero.attack, equipment.attack)
        except Errors.ImpossibleChange:
            SOS.SOSMessages.impossible_to_use()

        try:
            hero.defence = HelperFunc.ForAdventurerFuncs.possible_change(hero.defence, equipment.defence)
        except Errors.ImpossibleChange:
            SOS.SOSMessages.impossible_to_use()

        try:
            hero.hp = HelperFunc.ForAdventurerFuncs.possible_change(hero.hp, equipment.hp)
        except Errors.ImpossibleChange:
            SOS.SOSMessages.impossible_to_use()

        try:
            hero.mana = HelperFunc.ForAdventurerFuncs.possible_change(hero.mana, equipment.mana)
        except Errors.ImpossibleChange:
            SOS.SOSMessages.impossible_to_use()

        try:
            hero.magic_attack = HelperFunc.ForAdventurerFuncs.possible_change(hero.magic_attack, equipment.magic_attack)
        except Errors.ImpossibleChange:
            SOS.SOSMessages.impossible_to_use()

        hero.hero_active_skills = HelperFunc.ForArtefacts.skills_add(hero.hero_active_skills, equipment.key)
        hero.hero_active_skills[equipment.key].extend(equipment.active_skills)

        hero.hero_passive_skills = HelperFunc.ForArtefacts.skills_add(hero.hero_passive_skills, equipment.key)
        hero.hero_passive_skills[equipment.key].extend(equipment.passive_skills)

        AttentionMessages.successfully_done()

        return hero
