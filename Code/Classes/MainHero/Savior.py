from Code.BasicFuncs.Start.RecreateEverything import RecreateAdventurer
from Code.BasicFuncs.Finish.FinishGame import finish_it


class ReadHero:

    @staticmethod
    def read_it():
        return RecreateAdventurer.get_hero(False)

    @staticmethod
    def save_it():
        finish_it()

