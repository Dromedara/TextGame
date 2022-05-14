from COde_1.BasicFuncs.Game.BattelField.BattleSubFuncs import BattleChecker


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
    param_savior: {}

    battle_armor: {}

    def __init__(self, adventurer):
        self.attack = (adventurer.power + adventurer.speed) * adventurer.attack_coeff
        self.defence = adventurer.stamina * adventurer.defence_coeff
        self.hp = (adventurer.stamina + adventurer.power) * 10
        self.mana = (adventurer.wisdom + adventurer.intellect) * adventurer.mana_coeff
        self.magic_attack = (self.mana * self.attack) / 2

        self.hero_active_skills = {}
        self.hero_active_skills = BattleChecker.skills_add(self.hero_active_skills, 'basic')
        self.hero_active_skills = BattleChecker.skills_add(self.hero_active_skills, 'artefacts')
        self.hero_active_skills['basic'].extend(adventurer.active_skills)

        self.hero_passive_skills = {}
        self.hero_passive_skills = BattleChecker.skills_add(self.hero_passive_skills, 'basic')
        self.hero_passive_skills = BattleChecker.skills_add(self.hero_passive_skills, 'artefacts')
        self.hero_passive_skills['basic'].extend(adventurer.passive_skills)

        self.hero_long_baffs = {}
        self.tiks = {}

        self.param_savior = {
            'attack': [],
            'defence': [],
            'hp': [],
            'mana': [],
            'magic_attack': []
        }

        self.battle_armor = {
            'helmet': None,
            'bib': None,
            'pants': None
        }

    def remember_params(self):
        self.param_savior['attack'].append(self.attack)
        self.param_savior['defence'].append(self.defence)
        self.param_savior['hp'].append(self.hp)
        self.param_savior['mana'].append(self.mana)
        self.param_savior['magic_attack'].append(self.magic_attack)