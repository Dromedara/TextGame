from Code.Classes.People import Adventurer
import Code.Classes.Monsters as Monsters


class GetData:

    def __init__(self):
        pass

    @staticmethod
    def main_hero():
        f = open('SavingData/main_hero.txt', 'r')
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

        with open('SavingData/hero_active_skills.txt', 'r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                if len(line) != 0:
                    hero.active_skills.append(line[:-1])
            f.close()

        with open('SavingData/hero_passive_skills.txt', 'r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                if len(line) != 0:
                    hero.passive_skills.append(line[:-1])
            f.close()

        return hero

    @staticmethod
    def monster(monster_name):

        monsters = {
            'Chupakabra': Monsters.Chupakabra
        }

        with open('SavingData/monsters.txt', 'r') as f:
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
        with open('SavingData/adventures.txt', 'r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                adventure, monster_name = line.split()
                if adventure == adventure_name:
                    f.close()
                    return monster_name


class PassData:

    def __init__(self):
        pass

    @staticmethod
    def main_hero(hero):
        with open('SavingData/main_hero.txt', 'w') as f:
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

        with open('SavingData/hero_active_skills.txt', 'w') as f:
            f.seek(0)
            for i in hero.active_skills:
                f.write(str(i))
                f.write('\n')
            f.close()

        with open('SavingData/hero_passive_skills.txt', 'w') as f:
            f.seek(0)
            for i in hero.passive_skills:
                f.write(str(i))
                f.write('\n')
            f.close()






