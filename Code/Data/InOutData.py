from Code.Classes.People.People import Adventurer
import Code.Classes.Monsters.Monsters as Monsters
from Code.Classes.Artefacts.CreateArtefact import Creator as ArtefactCreator
from Code.Classes.Potions.CreatePotion import Creator as PotionCreator


class GetData:

    def __init__(self):
        pass

    @staticmethod
    def main_hero():
        f = open('Data/DataBase/main_hero.txt', 'r')
        name_of_val, name = f.readline().split()
        name_of_val, lvl = f.readline().split()
        name_of_val, gold = f.readline().split()
        name_of_val, exp = f.readline().split()
        name_of_val, lvl_ch_ed = f.readline().split()
        name_of_val, rise_coeff = f.readline().split()
        name_of_val, power = f.readline().split()
        name_of_val, speed = f.readline().split()
        name_of_val, wisdom = f.readline().split()
        name_of_val, intellect = f.readline().split()
        name_of_val, stamina = f.readline().split()
        name_of_val, free = f.readline().split()
        name_of_val, attack_coeff = f.readline().split()
        name_of_val, defence_coeff = f.readline().split()
        name_of_val, hp_coeff = f.readline().split()
        name_of_val, mana_coeff = f.readline().split()

        hero = Adventurer(name, int(lvl), int(gold), int(exp), float(lvl_ch_ed), float(rise_coeff), float(power),
                          float(speed), float(wisdom), float(intellect), float(stamina), float(free),
                          float(attack_coeff), float(defence_coeff), float(hp_coeff), float(mana_coeff))
        f.close()

        with open('Data/DataBase/hero_active_skills.txt', 'r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                hero.active_skills.append(line[:-1])
            f.close()

        with open('Data/DataBase/hero_passive_skills.txt', 'r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                hero.passive_skills.append(line[:-1])
            f.close()

        return hero

    @staticmethod
    def monster(monster_name):

        monsters = {
            'Chupakabra': Monsters.Chupakabra
        }

        with open('Data/DataBase/monsters.txt', 'r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                name, lvl = line.split()
                if name == monster_name:
                    f.close()
                    return monsters[monster_name](int(lvl))

    @staticmethod
    def monster_for_adventure(adventure_name):
        with open('Data/DataBase/adventures.txt', 'r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                adventure, monster_name = line.split()
                if adventure == adventure_name:
                    f.close()
                    return monster_name

    @staticmethod
    def artefacts():
        artefacts = []

        with open('Data/DataBase/artefacts.txt', 'r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                artefact = ArtefactCreator.create_artefact(line)
                artefacts.append(artefact)
            f.close()
        return artefacts

    @staticmethod
    def potions():
        potions = []

        with open('Data/DataBase/potions.txt', 'r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                potion = PotionCreator.create_potion(line)
                potions.append(potion)
            f.close()
        return potions


class PassData:

    def __init__(self):
        pass

    @staticmethod
    def main_hero(hero):
        with open('Data/DataBase/main_hero.txt', 'w') as f:
            f.seek(0)
            f.write('name: ' + str(hero.name) + '\n')
            f.write('lvl: ' + str(hero.lvl) + '\n')
            f.write('gold: ' + str(hero.gold) + '\n')
            f.write('exp: ' + str(hero.exp) + '\n')
            f.write('lvl_ch_edge: ' + str(hero.lvl_changing_edge) + '\n')
            f.write('rise_coeff: ' + str(hero.rise_coeff) + '\n')
            f.write('power: ' + str(hero.power) + '\n')
            f.write('speed: ' + str(hero.speed) + '\n')
            f.write('wisdom: ' + str(hero.wisdom) + '\n')
            f.write('intellect: ' + str(hero.intellect) + '\n')
            f.write('stamina: ' + str(hero.stamina) + '\n')
            f.write('free: ' + str(hero.free) + '\n')
            f.write('attack_coeff: ' + str(hero.attack_coeff) + '\n')
            f.write('defence_coeff: ' + str(hero.defence_coeff) + '\n')
            f.write('hp_coeff: ' + str(hero.hp_coeff) + '\n')
            f.write('mana_coeff: ' + str(hero.mana_coeff) + '\n')
            f.close()

        with open('Data/DataBase/hero_active_skills.txt', 'w') as f:
            f.seek(0)
            for i in hero.active_skills:
                f.write(str(i))
                f.write('\n')
            f.close()

        with open('Data/DataBase/hero_passive_skills.txt', 'w') as f:
            f.seek(0)
            for i in hero.passive_skills:
                f.write(str(i))
                f.write('\n')
            f.close()

    @staticmethod
    def artefacts(artefacts):
        with open('Data/DataBase/artefacts.txt', 'w') as f:
            f.seek(0)
            for artefact in artefacts:
                line = str(artefact.key) + ' '
                line += str(artefact.id) + ' ' 
                line += str(artefact.rarity) + ' ' 
                line += str(artefact.attack) + ' '
                line += str(artefact.defence) + ' '
                line += str(artefact.hp) + ' ' 
                line += str(artefact.mana) + ' ' 
                line += str(artefact.magic_attack)
                f.write(line)
                f.write('\n')
            f.close()

    @staticmethod
    def potions(potions):
        with open('Data/DataBase/potions.txt', 'w') as f:
            f.seek(0)
            for potion in potions:
                line = str(potion.key) + ' '
                line += str(potion.rarity) + ' '
                line += str(potion.attack) + ' '
                line += str(potion.defence) + ' '
                line += str(potion.hp) + ' '
                line += str(potion.mana) + ' '
                line += str(potion.magic_attack)
                f.write(line)
                f.write('\n')
            f.close()
