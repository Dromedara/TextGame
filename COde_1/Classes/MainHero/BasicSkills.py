from COde_1.BasicFuncs.Game.BattelField.BattleSubFuncs import BattleChecker


class AdventurerFuncs:

    @staticmethod
    def simple_punch(hero, monster):
        monster.hp -= (hero.attack - 0.8 * monster.defence)
        monster.defence = BattleChecker.params_change(monster.defence, 0.2 * hero.attack)
        return hero, monster
