import Code.BasicFuncs.Start.StartGame as StartGame
import Code.BasicFuncs.Game.PlayGame as PlayGame
import Code.BasicFuncs.Finish.FinishGame as FinishGame


def main():
    StartGame.start_it(first_activation=False)
    PlayGame.play_it()
    FinishGame.finish_it()


if __name__ == '__main__':
    main()
