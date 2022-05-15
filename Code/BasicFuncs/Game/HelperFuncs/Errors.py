class GameExceptions(Exception):
    pass


class NoHP(GameExceptions):

    message: str

    def __init__(self, message='You died!'):

        self.message = message
        super().__init__(self.message)


class NotPossibleToUse(GameExceptions):

    message: str

    def __init__(self, message='You are ot able to use it!'):

        self.message = message
        super().__init__(self.message)
