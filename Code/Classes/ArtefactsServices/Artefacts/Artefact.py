class Artefact:

    id: int
    rarity: int
    key: str
    attack: float
    defence: float
    hp: float
    mana: float
    magic_attack: float

    active_skills: []
    passive_skills: []

    def __init__(self):
        self.id = 0
        self.rarity = 0
        self.key = ''
        self.attack = 0
        self.defence = 0
        self.hp = 0
        self.mana = 0
        self.magic_attack = 0

        self.active_skills = []
        self.passive_skills = []

