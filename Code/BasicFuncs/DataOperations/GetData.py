import pandas as pd

from Code.Classes.MainHero.AdventurerRunner import Adventurer
from Code.Classes.Equipment.ArtefactsService.CreateArtefact import ArtefactCreator
from Code.Classes.Equipment.PotionsService.CreatePotions import PotionsCreator
from Code.Classes.Equipment.ArmorService.CreateArmor import ArmorCreator
from Code.Classes.AdventureDescription.CreateAdventure import AdventureCreator

import Code.Classes.Equipment.ArmorService.ArmorLinks as ArmorLinks
import Code.Classes.Equipment.IDCounter as ID

import Code.BasicFuncs.DataOperations.Paths as Paths
from Code.Classes.Monster import CreateMonster
from Code.BasicFuncs.Game.Guild import GuildLinks


def adventurer_creator(first_activation=True):
    if first_activation:
        df = pd.read_csv(Paths.paths['hero_first_activation'], index_col=0)
    else:
        df = pd.read_csv(Paths.paths['main_hero'], index_col=0)

    hero = Adventurer(_name=df.iloc[0]['name'],
                      lvl=int(df.iloc[0]['lvl']),
                      gold=int(df.iloc[0]['gold']),
                      exp=int(df.iloc[0]['exp']),
                      lvl_ch_ed=int(df.iloc[0]['lvl_ch_edge']),
                      rise_coeff=float(df.iloc[0]['rise_coeff']),
                      power=float(df.iloc[0]['power']),
                      speed=float(df.iloc[0]['speed']),
                      wisdom=float(df.iloc[0]['wisdom']),
                      intellect=float(df.iloc[0]['intellect']),
                      stamina=float(df.iloc[0]['stamina']),
                      free=int(df.iloc[0]['free']),
                      attack_coeff=float(df.iloc[0]['attack_coeff']),
                      defence_coeff=float(df.iloc[0]['defence_coeff']),
                      hp_coeff=float(df.iloc[0]['hp_coeff']),
                      mana_coeff=float(df.iloc[0]['mana_coeff']))
    return hero


def adventurer_skills(first_activation=True):
    if first_activation:
        return ['simple_punch'], []
    else:
        df_active = pd.read_csv(Paths.paths['hero_active_skills'], index_col=0)
        df_passive = pd.read_csv(Paths.paths['hero_passive_skills'], index_col=0)
        return df_active.active_skills.tolist(), df_passive.passive_skills.tolist()


def artefacts_creator(first_activation=True):
    artefacts = {}

    if not first_activation:
        df = pd.read_csv(Paths.paths['artefacts'], index_col=0)
        for i in range(len(df)):
            artefact = ArtefactCreator.create_artefact(key=df.iloc[i]['key'],
                                                       _id=int(df.iloc[i]['id']),
                                                       rarity=int(df.iloc[i]['rarity']),
                                                       attack=float(df.iloc[i]['attack']),
                                                       defence=float(df.iloc[i]['defence']),
                                                       hp=float(df.iloc[i]['hp']),
                                                       mana=float(df.iloc[i]['mana']),
                                                       magic_attack=float(df.iloc[i]['magic_attack']))
            artefacts[df.iloc[i]['id']] = artefact

    return artefacts


def potions_creator(first_activation=True):
    potions = {}

    if not first_activation:
        df = pd.read_csv(Paths.paths['potions'], index_col=0)
        for i in range(len(df)):
            potion = PotionsCreator.create_potion(key=df.iloc[i]['key'],
                                                  _id=int(df.iloc[i]['id']),
                                                  rarity=int(df.iloc[i]['rarity']),
                                                  tik=int(df.iloc[i]['tik']),
                                                  attack=float(df.iloc[i]['attack']),
                                                  defence=float(df.iloc[i]['defence']),
                                                  hp=float(df.iloc[i]['hp']),
                                                  mana=float(df.iloc[i]['mana']),
                                                  magic_attack=float(df.iloc[i]['magic_attack']))
            potions[df.iloc[i]['id']] = potion

    return potions


def armors_creator(first_activation=True):
    if first_activation:
        df = pd.read_csv(Paths.paths['armor_first_activation'], index_col=0)
    else:
        df = pd.read_csv(Paths.paths['armor'], index_col=0)

    armor = {}
    for key in ArmorLinks.parts_dict.keys():
        armor[key] = {}

    for i in range(len(df)):
        armor_part = ArmorCreator.create_armor(key=df.iloc[i]['key'],
                                               _id=int(df.iloc[i]['id']),
                                               rarity=int(df.iloc[i]['rarity']),
                                               attack=float(df.iloc[i]['attack']),
                                               defence=float(df.iloc[i]['defence']),
                                               hp=float(df.iloc[i]['hp']),
                                               mana=float(df.iloc[i]['mana']),
                                               magic_attack=float(df.iloc[i]['magic_attack']))

        for part in ArmorLinks.parts_dict.keys():
            if armor_part.key in ArmorLinks.parts_dict[part]:
                armor[part][armor_part.id] = armor_part

    return armor


def id_creator(first_activation):
    if not first_activation:
        df = pd.read_csv(Paths.paths['id'], index_col=0)
        ID.id_creator.id = int(df.iloc[0]['count'])


def battle_artefacts_creator(first_activation=True):
    artefacts = {}

    if not first_activation:
        df = pd.read_csv(Paths.paths['battle_artefacts'], index_col=0)
        for i in range(len(df)):
            artefact = ArtefactCreator.create_artefact(key=df.iloc[i]['key'],
                                                       _id=int(df.iloc[i]['id']),
                                                       rarity=int(df.iloc[i]['rarity']),
                                                       attack=float(df.iloc[i]['attack']),
                                                       defence=float(df.iloc[i]['defence']),
                                                       hp=float(df.iloc[i]['hp']),
                                                       mana=float(df.iloc[i]['mana']),
                                                       magic_attack=float(df.iloc[i]['magic_attack']))
            artefacts[df.iloc[i]['id']] = artefact

    return artefacts


def battle_armors_creator(first_activation=True):
    if first_activation:
        df = pd.read_csv(Paths.paths['armor_first_activation'], index_col=0)
    else:
        df = pd.read_csv(Paths.paths['battle_armor'], index_col=0)

    armor = {}
    for key in ArmorLinks.parts_dict.keys():
        armor[key] = None

    for i in range(len(df)):
        armor_part = ArmorCreator.create_armor(key=df.iloc[i]['key'],
                                               _id=int(df.iloc[i]['id']),
                                               rarity=int(df.iloc[i]['rarity']),
                                               attack=float(df.iloc[i]['attack']),
                                               defence=float(df.iloc[i]['defence']),
                                               hp=float(df.iloc[i]['hp']),
                                               mana=float(df.iloc[i]['mana']),
                                               magic_attack=float(df.iloc[i]['magic_attack']))

        for part_name in ArmorLinks.parts_dict.keys():
            if armor_part.key in ArmorLinks.parts_dict[part_name]:
                armor[part_name] = armor_part
                break

    return armor


def battle_potions_creator(first_activation=True):
    potions = {}

    if not first_activation:
        df = pd.read_csv(Paths.paths['battle_potions'], index_col=0)
        for i in range(len(df)):
            potion = PotionsCreator.create_potion(key=df.iloc[i]['key'],
                                                  _id=int(df.iloc[i]['id']),
                                                  rarity=int(df.iloc[i]['rarity']),
                                                  tik=int(df.iloc[i]['tik']),
                                                  attack=float(df.iloc[i]['attack']),
                                                  defence=float(df.iloc[i]['defence']),
                                                  hp=float(df.iloc[i]['hp']),
                                                  mana=float(df.iloc[i]['mana']),
                                                  magic_attack=float(df.iloc[i]['magic_attack']))
            potions[df.iloc[i]['id']] = potion

    return potions


def monster_creator(adventure_name, serial_num):
    df = pd.read_csv(Paths.paths['monster'])
    for i in range(len(df)):
        if df.iloc[i]['adventure'] == adventure_name and df.iloc[i]['serial_number'] == serial_num:
            monster = CreateMonster.Creator.create_monster(key=df.iloc[i]['name'], lvl=df.iloc[i]['lvl'])
            return monster


def adventure_creator():
    df = pd.read_csv(Paths.paths['adventures'])
    for i in range(len(df)):
        adventure = AdventureCreator.create_adventure(key=df.iloc[i]['name'],
                                                      gold=int(df.iloc[i]['gold_award']),
                                                      exp=int(df.iloc[i]['exp_award']),
                                                      description=df.iloc[i]['description'],
                                                      done=bool(df.iloc[i]['done']),
                                                      blocked=bool(df.iloc[i]['blocked']))
        GuildLinks.adventures_dict[adventure.key] = adventure
        GuildLinks.adventures_names.append(adventure.key)

