class Adventure:

    key: str
    description: str
    exp: int
    gold: int
    blocked: bool
    done: bool

    def __init__(self, key: str = '', description: str = 'Unknown', exp: int = 0, gold: int = 0,
                 blocked: bool = True, done: bool = True):

        self.key = key
        self.description = description
        self.exp = exp
        self.gold = gold
        self.blocked = blocked
        self.done = done
