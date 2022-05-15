import pandas as pd
import Code.BasicFuncs.Finish.SaveData.Paths as Paths
from Code.BasicFuncs.Game.Warehouse.Inventory.Main import main_inventory
import Code.Classes.Equipment.IDCounter as ID


def save_hero(hero):

    df = pd.DataFrame({
        'name': hero.name,
        'lvl': hero.lvl,
        'gold': hero.gold,
        'exp': hero.exp,
        'lvl_ch_edge': hero.lvl_changing_edge,
        'rise_coeff': hero.rise_coeff,
        'power': hero.power,
        'speed': hero.speed,
        'wisdom': hero.wisdom,
        'intellect': hero.intellect,
        'stamina': hero.stamina,
        'free': hero.stamina,
        'attack_coeff': hero.attack_coeff,
        'defence_coeff': hero.defence_coeff,
        'hp_coeff': hero.hp_coeff,
        'mana_coeff': hero.mana_coeff
        },
        index=[0])

    df.to_csv(Paths.paths['main_hero'])

    # active skills
    df = pd.DataFrame({
        'active_skills': hero.active_skills
    })
    df.to_csv(Paths.paths['hero_active_skills'])

    # passive skills
    df = pd.DataFrame({
        'passive_skills': hero.passive_skills
    })
    df.to_csv(Paths.paths['hero_passive_skills'])


def save_armors():
    param_dict = {
        'key': [],
        'id': [],
        'rarity': [],
        'attack': [],
        'defence': [],
        'hp': [],
        'mana': [],
        'magic_attack': []
    }

    for part in main_inventory.armor_dict.keys():
        for key in main_inventory.armor_dict[part].keys():
            param_dict['key'].append(main_inventory.armor_dict[part][key].key)
            param_dict['id'].append(main_inventory.armor_dict[part][key].id)
            param_dict['rarity'].append(main_inventory.armor_dict[part][key].rarity)
            param_dict['attack'].append(main_inventory.armor_dict[part][key].attack)
            param_dict['defence'].append(main_inventory.armor_dict[part][key].defence)
            param_dict['hp'].append(main_inventory.armor_dict[part][key].hp)
            param_dict['mana'].append(main_inventory.armor_dict[part][key].mana)
            param_dict['magic_attack'].append(main_inventory.armor_dict[part][key].magic_attack)

    df = pd.DataFrame(param_dict)
    df.to_csv(Paths.paths['armor'])


def save_artefacts():
    param_dict = {
        'key': [],
        'id': [],
        'rarity': [],
        'attack': [],
        'defence': [],
        'hp': [],
        'mana': [],
        'magic_attack': []
    }

    for key in main_inventory.artefacts_dict.keys():
        param_dict['key'].append(main_inventory.artefacts_dict[key].key)
        param_dict['id'].append(main_inventory.artefacts_dict[key].id)
        param_dict['rarity'].append(main_inventory.artefacts_dict[key].rarity)
        param_dict['attack'].append(main_inventory.artefacts_dict[key].attack)
        param_dict['defence'].append(main_inventory.artefacts_dict[key].defence)
        param_dict['hp'].append(main_inventory.artefacts_dict[key].hp)
        param_dict['mana'].append(main_inventory.artefacts_dict[key].mana)
        param_dict['magic_attack'].append(main_inventory.artefacts_dict[key].magic_attack)

    df = pd.DataFrame(param_dict)
    df.to_csv(Paths.paths['artefacts'])


def save_potions():
    param_dict = {
        'key': [],
        'id': [],
        'rarity': [],
        'tik': [],
        'attack': [],
        'defence': [],
        'hp': [],
        'mana': [],
        'magic_attack': []
    }

    for key in main_inventory.potions_dict.keys():
        for potion in main_inventory.potions_dict[key]:
            param_dict['key'].append(potion.key)
            param_dict['id'].append(potion.id)
            param_dict['rarity'].append(potion.rarity)
            param_dict['tik'].append(potion.tik)
            param_dict['attack'].append(potion.attack)
            param_dict['defence'].append(potion.defence)
            param_dict['hp'].append(potion.hp)
            param_dict['mana'].append(potion.mana)
            param_dict['magic_attack'].append(potion.magic_attack)

    df = pd.DataFrame(param_dict)
    df.to_csv(Paths.paths['potions'])


def save_id():
    df = pd.read_csv(Paths.paths['id'])
    df.iloc[0]['count'] = ID.id_creator.id
    df.to_csv(Paths.paths['id'])
