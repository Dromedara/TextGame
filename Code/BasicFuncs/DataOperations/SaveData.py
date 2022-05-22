import pandas as pd
import Code.BasicFuncs.DataOperations.Paths as Paths
from Code.BasicFuncs.Game.Warehouse.Inventory.Main import main_inventory
from Code.BasicFuncs.Game.Warehouse.Inventory.Battle import battle_inventory
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
        param_dict['key'].append(main_inventory.potions_dict[key].key)
        param_dict['id'].append(main_inventory.potions_dict[key].id)
        param_dict['rarity'].append(main_inventory.potions_dict[key].rarity)
        param_dict['tik'].append(main_inventory.potions_dict[key].tik)
        param_dict['attack'].append(main_inventory.potions_dict[key].attack)
        param_dict['defence'].append(main_inventory.potions_dict[key].defence)
        param_dict['hp'].append(main_inventory.potions_dict[key].hp)
        param_dict['mana'].append(main_inventory.potions_dict[key].mana)
        param_dict['magic_attack'].append(main_inventory.potions_dict[key].magic_attack)

    df = pd.DataFrame(param_dict)
    df.to_csv(Paths.paths['potions'])


def save_id():
    df = pd.DataFrame({'count': [ID.id_creator.id]})
    df.to_csv(Paths.paths['id'])


def save_battle_armors():
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

    for part in battle_inventory.curr_armors.keys():
        if battle_inventory.curr_armors[part] is not None:
            param_dict['key'].append(battle_inventory.curr_armors[part].key)
            param_dict['id'].append(battle_inventory.curr_armors[part].id)
            param_dict['rarity'].append(battle_inventory.curr_armors[part].rarity)
            param_dict['attack'].append(battle_inventory.curr_armors[part].attack)
            param_dict['defence'].append(battle_inventory.curr_armors[part].defence)
            param_dict['hp'].append(battle_inventory.curr_armors[part].hp)
            param_dict['mana'].append(battle_inventory.curr_armors[part].mana)
            param_dict['magic_attack'].append(battle_inventory.curr_armors[part].magic_attack)

    df = pd.DataFrame(param_dict)
    df.to_csv(Paths.paths['battle_armor'])


def save_battle_artefacts():
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

    for key in battle_inventory.curr_artefacts.keys():
        param_dict['key'].append(battle_inventory.curr_artefacts[key].key)
        param_dict['id'].append(battle_inventory.curr_artefacts[key].id)
        param_dict['rarity'].append(battle_inventory.curr_artefacts[key].rarity)
        param_dict['attack'].append(battle_inventory.curr_artefacts[key].attack)
        param_dict['defence'].append(battle_inventory.curr_artefacts[key].defence)
        param_dict['hp'].append(battle_inventory.curr_artefacts[key].hp)
        param_dict['mana'].append(battle_inventory.curr_artefacts[key].mana)
        param_dict['magic_attack'].append(battle_inventory.curr_artefacts[key].magic_attack)

    df = pd.DataFrame(param_dict)
    df.to_csv(Paths.paths['battle_artefacts'])


def save_battle_potions():
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

    for key in battle_inventory.curr_potions.keys():
        param_dict['key'].append(battle_inventory.curr_potions[key].key)
        param_dict['id'].append(battle_inventory.curr_potions[key].id)
        param_dict['rarity'].append(battle_inventory.curr_potions[key].rarity)
        param_dict['tik'].append(battle_inventory.curr_potions[key].tik)
        param_dict['attack'].append(battle_inventory.curr_potions[key].attack)
        param_dict['defence'].append(battle_inventory.curr_potions[key].defence)
        param_dict['hp'].append(battle_inventory.curr_potions[key].hp)
        param_dict['mana'].append(battle_inventory.curr_potions[key].mana)
        param_dict['magic_attack'].append(battle_inventory.curr_potions[key].magic_attack)

    df = pd.DataFrame(param_dict)
    df.to_csv(Paths.paths['battle_potions'])
