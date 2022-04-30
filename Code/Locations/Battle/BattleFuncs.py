from Code.Classes.MainCharacter.BattleMod import BattleMod
import Code.Data.InOutData as Characters
from Code.Classes.ArtefactsServices.WearingArtefacts import Wearing
import Code.Subfunctions.Messages.SOS as SOS
from Code.Subfunctions.Messages.Attention import AttentionMessages
import Code.Locations.Battle.BattleSubFuncs as SubFuncs
from Code.Data.InOutData import GetData


def end(hero):
    if hero.hp <= 0:
        SOS.SOSMessages.lose_battle()
        return 'lose'

    AttentionMessages.win()
    return 'win'


def check(hero, monster):
    if hero.hp <= 0 or monster.hp <= 0:
        return True
    return False


class Prepearing:
    @staticmethod
    def prepare_hero(adventurer):

        hero = BattleMod(adventurer)

        while True:
            wearing_artefact = SubFuncs.Choose.choose_artefacts()

            if wearing_artefact is None:
                break
            hero = Wearing.get_equipment(hero, wearing_artefact)

        return hero

    @staticmethod
    def prepare_monster(adventure_name, serial_num=1):

        monster = Characters.GetData.monster(adventure_name=adventure_name, serial_num=serial_num)

        return monster

    @staticmethod
    def prepare_artefacts():
        artefacts = GetData.artefacts()
        return artefacts

    @staticmethod
    def prepare_potions():
        potions = GetData.potions()
        return potions


class Other:
    @staticmethod
    def show(hero):
        print(hero.hero_active_skills)
        print(hero.hero_passive_skills)
        print(f"hp: {hero.hp},\nattack: {hero.attack},\ndefence: {hero.defence},\nmana: {hero.mana},\nmagic attack: {hero.magic_attack}\n")
