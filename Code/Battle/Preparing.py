from Code.Classes.BattleMod import BattleMod
import Code.SavingData.Characters as Characters
import Code.Classes.Artefacts as Artefacts


def prepare_hero(adventurer):

    hero = BattleMod(adventurer)

    # выбор снаряжения?

    armor = Artefacts.CharmedIronArmor(1, 1)
    sword = Artefacts.CharmedSword(1, 1)
    amulet = Artefacts.SimpleMagicAmulet(1, 1)

    hero.get_equipment(armor)
    print('armor')
    hero.get_equipment(sword)
    print('sword')
    hero.get_equipment(amulet)
    print('amulet')

    return hero


def prepare_monster(adventure_name):

    monster_name = Characters.GetData.monster_for_adventure(adventure_name)
    monster = Characters.GetData.monster(monster_name)

    return monster
