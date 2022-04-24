import Code.SavingData.Characters as Data
from Code.Classes.BattleMod import BattleMod
import Code.Classes.Artefacts as Artefacts


def main():
    hero = Data.GetData.main_hero()  # получить гг

    print(hero.name)

    hero.add_passive_skill('attack')

    simp_armor = Artefacts.SimpleIronArmor()
    iron_armor = Artefacts.CharmedIronArmor()
    battle_hero = BattleMod(hero)

    print(battle_hero.warrior_passive_skills)
    print(iron_armor.passive_skills)

    if battle_hero.get_equipment(iron_armor):
        print(battle_hero.warrior_passive_skills)

    monster = Data.GetData.monster('Chupakabra')  # получить монстра

    Data.PassData.main_hero(hero)  # записать гг


if __name__ == '__main__':
    main()
