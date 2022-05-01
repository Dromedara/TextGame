from Code.Subfunctions.Errors import NoHP


class Checker:

    def __init__(self):
        pass

    @staticmethod
    def exp_change(param, edge):
        if param < edge:
            return False
        return True
