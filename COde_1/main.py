import COde_1.BasicFuncs.Start.StartGame as StartGame
import COde_1.BasicFuncs.Game.PlayGame as PlayGame
import COde_1.BasicFuncs.Finish.FinishGame as FinishGame


def main():
    hero = StartGame.start_it()
    print(hero.name)
    hero = PlayGame.play_it(hero)
    FinishGame.finish_it(hero)


if __name__ == '__main__':
    main()
