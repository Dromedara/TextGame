import Code.BasicFuncs.Start.StartGame as StartGame
import Code.BasicFuncs.Game.PlayGame as PlayGame
import Code.BasicFuncs.Finish.FinishGame as FinishGame


def main():
    hero = StartGame.start_it(first_activation=False)
    print(hero.name)
    hero = PlayGame.play_it(hero)
    FinishGame.finish_it(hero)


if __name__ == '__main__':
    main()
