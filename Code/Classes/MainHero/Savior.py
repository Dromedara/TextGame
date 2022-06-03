from Code.BasicFuncs.Start.RecreateEverything import RecreateAdventurer
from Code.BasicFuncs.Finish.FinishGame import finish_it
from Code.BasicFuncs.DataOperations import SaveData


class ReadHero:

    @staticmethod
    def read_it():
        return RecreateAdventurer.get_hero(False)

    @staticmethod
    def save_it(hero):
        SaveData.save_hero(hero)
        finish_it()

