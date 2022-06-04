from Code.BasicFuncs.Game.BattelField.BattleSubFuncs import BattleChecker


class AdventurerFuncs:

    @staticmethod
    def simple_punch(hero, monster):
        monster.hp = BattleChecker.params_change(monster.defence, -(hero.attack - 0.8 * monster.defence), hero.param_savior['hp'][0])
        monster.defence = BattleChecker.params_change(monster.defence, -(0.2 * hero.attack), hero.param_savior['defence'][0])
        return hero, monster
