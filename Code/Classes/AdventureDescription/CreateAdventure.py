from Code.Classes.AdventureDescription.Adventure import Adventure


class AdventureCreator:

    @staticmethod
    def create_adventure(key, description, exp, gold, blocked, done):

        adventure = Adventure(key=key, description=description, exp=exp, gold=gold, blocked=blocked, done=done)

        return adventure

