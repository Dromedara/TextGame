class GameExceptions(Exception):
    pass


class ImpossibleChange(GameExceptions):

    message: str

    def __init__(self, message='It is not possible to change this such a way!'):

        self.message = message
        super().__init__(self.message)

