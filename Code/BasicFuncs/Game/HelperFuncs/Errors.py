class GameExceptions(Exception):
    pass


class NotPossibleToUse(GameExceptions):

    message: str

    def __init__(self, message='You are ot able to use it!'):

        self.message = message
        super().__init__(self.message)
