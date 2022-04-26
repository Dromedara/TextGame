import Code.Subfunctions.HelperFunc as HelperFunc
import Code.Subfunctions.Errors as Errors
import Code.Subfunctions.Messages.SOS as SOS
from Code.Subfunctions.Messages.Attention import AttentionMessages


class BattleMod:

    attack: float
    defence: float
    hp: float
    mana: float
    magic_attack: float

    hero_active_skills: {}
    hero_passive_skills: {}

    checker = HelperFunc.ForAdventurerFuncs()

    def __init__(self, adventurer):
        self.attack = (adventurer.power + adventurer.speed) * adventurer.attack_coeff
        self.defence = adventurer.stamina * adventurer.defence_coeff
        self.hp = (adventurer.stamina + adventurer.power) * 10
        self.mana = (adventurer.wisdom + adventurer.intellect) * adventurer.mana_coeff
        self.magic_attack = (self.mana * self.attack) / 2

        self.hero_active_skills = {}
        self.hero_active_skills = self.checker.skills_add(self.hero_active_skills, 'basic')
        self.hero_active_skills['basic'].extend(adventurer.active_skills)
        self.hero_passive_skills = {}
        self.hero_passive_skills = self.checker.skills_add(self.hero_passive_skills, 'basic')
        self.hero_passive_skills['basic'].extend(adventurer.passive_skills)

    def get_equipment(self, equipment):

        try:
            self.attack = self.checker.possible_change(self.attack, equipment.attack)
        except Errors.ImpossibleChange:
            SOS.SOSMessages.impossible_to_use()
            return False

        try:
            self.defence = self.checker.possible_change(self.defence, equipment.defence)
        except Errors.ImpossibleChange:
            SOS.SOSMessages.impossible_to_use()
            return False

        try:
            self.hp = self.checker.possible_change(self.hp, equipment.hp)
        except Errors.ImpossibleChange:
            SOS.SOSMessages.impossible_to_use()
            return False

        try:
            self.mana = self.checker.possible_change(self.mana, equipment.mana)
        except Errors.ImpossibleChange:
            SOS.SOSMessages.impossible_to_use()
            return False

        try:
            self.magic_attack = self.checker.possible_change(self.magic_attack, equipment.magic_attack)
        except Errors.ImpossibleChange:
            SOS.SOSMessages.impossible_to_use()
            return False

        self.hero_active_skills = self.checker.skills_add(self.hero_active_skills, equipment.key)
        self.hero_active_skills[equipment.key].extend(equipment.active_skills)

        self.hero_passive_skills = self.checker.skills_add(self.hero_passive_skills, equipment.key)
        self.hero_passive_skills[equipment.key].extend(equipment.passive_skills)

        AttentionMessages.successfully_done()
        return True
