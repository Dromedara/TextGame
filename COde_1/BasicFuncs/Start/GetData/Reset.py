import pandas as pd

from COde_1.Classes.MainHero.AdventurerRunner import Adventurer
from COde_1.Classes.Equipment.ArtefactsService.CreateArtefact import ArtefactCreator
from COde_1.Classes.Equipment.PotionsService.CreatePotions import PotionsCreator
from COde_1.Classes.Equipment.ArmorService.CreateArmor import ArmorCreator
import COde_1.Classes.Equipment.ArmorService.ArmorLinks as ArmorLinks

from COde_1.BasicFuncs.Game.Warehouse.InventorySubFuncs import InventoryChecker
from COde_1.BasicFuncs.Game.Warehouse.Inventory.Armor import ArmorInventory

import COde_1.BasicFuncs.Start.GetData.Paths as Paths


def adventurer_creator(first_activation=True):
    if first_activation:
        df = pd.read_csv(Paths.paths['hero_first_activation'], index_col=0)
    else:
        df = pd.read_csv(Paths.paths['main_hero'], index_col=0)

    hero = Adventurer(_name=df.iloc[0]['name'],
                      lvl=int(df.iloc[0]['lvl']),
                      gold=int(df.iloc[0]['gold']),
                      exp=int(df.iloc[0]['exp']),
                      lvl_ch_ed=float(df.iloc[0]['lvl_ch_edge']),
                      rise_coeff=float(df.iloc[0]['rise_coeff']),
                      power=float(df.iloc[0]['power']),
                      speed=float(df.iloc[0]['speed']),
                      wisdom=float(df.iloc[0]['wisdom']),
                      intellect=float(df.iloc[0]['intellect']),
                      stamina=float(df.iloc[0]['stamina']),
                      free=float(df.iloc[0]['free']),
                      attack_coeff=float(df.iloc[0]['attack_coeff']),
                      defence_coeff=float(df.iloc[0]['defence_coeff']),
                      hp_coeff=float(df.iloc[0]['hp_coeff']),
                      mana_coeff=float(df.iloc[0]['mana_coeff']))
    return hero


def adventurer_skills(first_activation=True):
    if first_activation:
        return [], []
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
            potions = InventoryChecker.add_potion(potions, df.iloc[i]['key'])
            potions[df.iloc[i]['key']].append(potion)

    return potions


def armors_creator(first_activation=True):
    if first_activation:
        df = pd.read_csv(Paths.paths['armor_first_activation'], index_col=0)
    else:
        df = pd.read_csv(Paths.paths['armor'], index_col=0)

    armor = {
            'helmet': {},
            'bib': {},
            'pants': {}
        }

    for i in range(len(df)):
        armor_part = ArmorCreator.create_armor(key=df.iloc[i]['key'],
                                               _id=int(df.iloc[i]['id']),
                                               rarity=int(df.iloc[i]['rarity']),
                                               attack=float(df.iloc[i]['attack']),
                                               defence=float(df.iloc[i]['defence']),
                                               hp=float(df.iloc[i]['hp']),
                                               mana=float(df.iloc[i]['mana']),
                                               magic_attack=float(df.iloc[i]['magic_attack']))

        if armor_part.key in ArmorLinks.helmet_list:
            armor['helmet'][armor_part.id] = armor_part
        if armor_part.key in ArmorLinks.bib_list:
            armor['bib'][armor_part.id] = armor_part
        if armor_part.key in ArmorLinks.pants_list:
            armor['pants'][armor_part.id] = armor_part

    return armor
