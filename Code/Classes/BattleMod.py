import Code.Checking.CheckClassFunctions as CheckClassFunction
import Code.Checking.Errors as Errors
import Code.Checking.SOS as SOS


class BattleMod:

    attack: float
    defence: float
    hp: float
    mana: float
    magic_attack: float

    warrior_active_skills: {}
    warrior_passive_skills: {}

    checker = CheckClassFunction.CheckAdventurerFuncs

    def __init__(self, adventurer):
        self.attack = (adventurer.power + adventurer.speed) * adventurer.attack_coeff
        self.defence = adventurer.endurance * adventurer.defence_coeff
        self.hp = adventurer.endurance + adventurer.power
        self.mana = (adventurer.wisdom+adventurer.intellect) * adventurer.mana_coeff
        self.magic_attack = self.mana * self.attack

        self.warrior_active_skills = {}
        self.warrior_active_skills = self.checker.skills_add(self.warrior_active_skills, 'basic')
        self.warrior_active_skills['basic'].extend(adventurer.active_skills)
        self.warrior_passive_skills = {}
        self.warrior_passive_skills = self.checker.skills_add(self.warrior_passive_skills, 'basic')
        self.warrior_passive_skills['basic'].extend(adventurer.passive_skills)

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

        self.warrior_active_skills = self.checker.skills_add(self.warrior_active_skills, equipment.key)
        self.warrior_active_skills[equipment.key].extend(equipment.active_skills)

        self.warrior_passive_skills = self.checker.skills_add(self.warrior_passive_skills, equipment.key)
        self.warrior_passive_skills[equipment.key].extend(equipment.passive_skills)

        return True
