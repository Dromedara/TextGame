import random

import Code.Classes.MainHero.AdventurerLinks as AdventurerLinks
import Code.Classes.Equipment.ArtefactsService.ArtefactsLinks as ArtefactsLinks
import Code.Classes.Monster.MonsterLinks as MonsterLinks


class PassiveActions:

    @staticmethod
    def run_it(hero, monster):

        for skill in hero.hero_passive_skills['basic']:
            hero, monster = AdventurerLinks.passive_adventurer_dict[skill](hero, monster)

        for skill in hero.hero_passive_skills['artefacts']:
            hero, monster = ArtefactsLinks.passive_artefact_dict[skill](hero, monster)

        return hero, monster


class ActiveActions:

    @staticmethod
    def run_it(hero, monster, choice):

        if choice in ArtefactsLinks.active_artefact_dict.keys():
            hero, monster = ArtefactsLinks.active_artefact_dict[choice](hero, monster)
        else:
            hero, monster = AdventurerLinks.active_adventurer_dict[choice](hero, monster)

        return hero, monster


class MonsterActions:

    @staticmethod
    def run_it(hero, monster):

        hero, monster = MonsterActions.active(hero, monster)

        monster = MonsterActions.passive(monster)

        return hero, monster

    @staticmethod
    def passive(monster):
        for action in monster.passive_skill:
            monster = MonsterLinks.passive_skills_dict[action](monster)
        return monster

    @staticmethod
    def active(hero, monster):
        action = random.randrange(0, len(monster.active_skill), 1)
        return MonsterLinks.active_skills_dict[monster.active_skill[action]](hero, monster)

