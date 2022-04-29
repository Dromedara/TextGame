from Code.Classes.MainCharacter.Adventurer import Adventurer
from Code.Classes.Monsters.CreateMonster import Creator as MonsterCreator
from Code.Classes.ArtefactsServices.CreateArtefact import Creator as ArtefactCreator
from Code.Classes.PotionsServices.CreatePotion import Creator as PotionCreator
import pandas as pd


def main():
    artefacts = GetData.artefacts()
    print(artefacts)


class GetData:

    def __init__(self):
        pass

    @staticmethod
    def main_hero(index=0):

        # parameters
        df = pd.read_csv('Data/DataBase/main_hero.csv', index_col=0)

        hero = Adventurer(df.iloc[index]['name'],
                          int(df.iloc[index]['lvl']),
                          int(df.iloc[index]['gold']),
                          int(df.iloc[index]['exp']),
                          int(df.iloc[index]['lvl_ch_edge']),
                          float(df.iloc[index]['rise_coeff']),
                          float(df.iloc[index]['power']),
                          float(df.iloc[index]['speed']),
                          float(df.iloc[index]['wisdom']),
                          float(df.iloc[index]['intellect']),
                          float(df.iloc[index]['stamina']),
                          float(df.iloc[index]['free']),
                          float(df.iloc[index]['attack_coeff']),
                          float(df.iloc[index]['defence_coeff']),
                          float(df.iloc[index]['hp_coeff']),
                          float(df.iloc[index]['mana_coeff']))

        df = df.drop(df.shape[0] - 1, axis=0)
        df.to_csv('Data/DataBase/main_hero.csv')

        # active skills
        if index:
            df = pd.DataFrame({'active_skills': []})
        else:
            df = pd.read_csv('Data/DataBase/hero_active_skills.csv', index_col=0)

        hero.active_skills = df.active_skills.tolist()

        # passive skills
        if index:
            df = pd.DataFrame({'passive_skills': []})
        else:
            df = pd.read_csv('Data/DataBase/hero_passive_skills.csv', index_col=0)

        hero.passive_skills = df.passive_skills.tolist()

        return hero

    @staticmethod
    def monster(adventure_name='FisrtAdventure', serial_num=1):

        df = pd.read_csv('Data/DataBase/monsters.csv', index_col=0)
        for i in range(len(df)):
            if df.iloc[i]['adventure'] == adventure_name and df.iloc[i]['serial_number'] == serial_num:
                return MonsterCreator.create_monster(df.iloc[i]['name'], (int(df.iloc[i]['lvl'])))

    @staticmethod
    def artefacts():
        artefacts = []

        df = pd.read_csv('DataBase/artefacts.csv', index_col=0)
        for i in range(len(df)):
            artefact = ArtefactCreator.create_artefact(key=df.iloc[i]['key'],
                                                       id=int(df.iloc[i]['id']),
                                                       rarity=int(df.iloc[i]['rarity']),
                                                       attack=float(df.iloc[i]['attack']),
                                                       defence=float(df.iloc[i]['defence']),
                                                       hp=float(df.iloc[i]['hp']),
                                                       mana=float(df.iloc[i]['mana']),
                                                       magic_attack=float(df.iloc[i]['magic_attack']))
            artefacts.append(artefact)

        return artefacts

    @staticmethod
    def potions():
        potions = []

        df = pd.read_csv('DataBase/potions.csv', index_col=0)
        for i in range(len(df)):
            potion = PotionCreator.create_potion(key=int(df.iloc[i]['key']),
                                                 rarity=int(df.iloc[i]['rarity']),
                                                 tik=int(df.iloc[i]['tik']),
                                                 attack=float(df.iloc[i]['attack']),
                                                 defence=float(df.iloc[i]['defence']),
                                                 hp=float(df.iloc[i]['hp']),
                                                 mana=float(df.iloc[i]['mana']),
                                                 magic_attack=float(df.iloc[i]['magic_attack']))
            potions.append(potion)

        return potions


class PassData:

    def __init__(self):
        pass

    @staticmethod
    def main_hero(hero):
        df = pd.read_csv('Data/DataBase/main_hero.csv', index_col=0)
        save_hero = {
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
        }

        df = df.append(save_hero, ignore_index=True)
        df.to_csv('Data/DataBase/main_hero.csv')

        # active skills
        df = pd.DataFrame({
          'active_skills': hero.active_skills
        })
        df.to_csv('Data/DataBase/hero_active_skills.csv')

        # passive skills
        df = pd.DataFrame({
            'passive_skills': hero.active_skills
        })
        df.to_csv('Data/DataBase/hero_passive_skills.csv')

    @staticmethod
    def artefacts(artefacts):

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

        for artefact in artefacts:
            param_dict['key'].append(artefact.key)
            param_dict['id'].append(artefact.id)
            param_dict['rarity'].append(artefact.rarity)
            param_dict['attack'].append(artefact.attack)
            param_dict['defence'].append(artefact.defence)
            param_dict['hp'].append(artefact.hp)
            param_dict['mana'].append(artefact.mana)
            param_dict['magic_attack'].append(artefact.magic_attack)

        df = pd.DataFrame(param_dict)
        df.to_csv('DataBase/artefacts.csv')

    @staticmethod
    def potions(potions):
        param_dict = {
            'key': [],
            'rarity': [],
            'tik': [],
            'attack': [],
            'defence': [],
            'hp': [],
            'mana': [],
            'magic_attack': []
        }

        for potion in potions:
            param_dict['key'].append(potion.key)
            param_dict['rarity'].append(potion.rarity)
            param_dict['tik'].append(potion.tik)
            param_dict['attack'].append(potion.attack)
            param_dict['defence'].append(potion.defence)
            param_dict['hp'].append(potion.hp)
            param_dict['mana'].append(potion.mana)
            param_dict['magic_attack'].append(potion.magic_attack)

        df = pd.DataFrame(param_dict)
        df.to_csv('DataBase/potions.csv')


if __name__ == '__main__':
    main()
