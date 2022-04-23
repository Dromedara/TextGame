import random


class Human:

    name: str
    lvl: int
    gold: int

    def __init__(self, _name='?'):
        self.name = _name
        self.lvl = 1
        self.gold = 0


class Adventurer(Human):

    exp: int
    power: float
    speed: float
    wisdom: float
    intellect: float
    endurance: float

    skills: []

    def __init__(self, _name='?'):
        super().__init__()
        self.name = _name
        self.gold += 10


class Merchant(Human):

    decency: int

    def __init__(self, _name='?'):
        super().__init__()
        self.name = _name
        self.decency = random.randrange(0, 100, 1)