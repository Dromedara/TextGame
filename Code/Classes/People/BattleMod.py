import Code.Subfunctions.HelperFunc as HelperFunc


class BattleMod:

    attack: float
    defence: float
    hp: float
    mana: float
    magic_attack: float

    hero_active_skills: {}
    hero_passive_skills: {}
    hero_long_baffs: {}
    tiks: {}

    checker = HelperFunc.ForArtefacts()

    def __init__(self, adventurer):
        self.attack = (adventurer.power + adventurer.speed) * adventurer.attack_coeff
        self.defence = adventurer.stamina * adventurer.defence_coeff
        self.hp = (adventurer.stamina + adventurer.power) * 10
        self.mana = (adventurer.wisdom + adventurer.intellect) * adventurer.mana_coeff
        self.magic_attack = (self.mana * self.attack) / 2

        self.hero_active_skills = {}
        self.hero_active_skills = self.checker.skills_add(self.hero_active_skills, 'basic')
        self.hero_active_skills['basic'].extend(adventurer.active_skills)

        self.hero_passive_skills = []
        self.hero_passive_skills.extend(adventurer.passive_skills)

        self.hero_long_baffs = {}
        self.tiks = {}
