from Code.Classes.People import Adventurer
import Code.Classes.Monsters as Monsters


class GetData:

    def __init__(self):
        pass

    @staticmethod
    def main_hero():
        f = open('Code/SavingData/main_hero.txt', 'r')
        line = f.readline()
        name, lvl, gold, exp, lvl_ch_ed, rise_coeff, power, speed, wisdom, \
            intellect, endurance, attack_coeff, defence_coeff, hp_coeff, mana_coeff = line.split()

        hero = Adventurer(name, int(lvl), int(gold), int(exp), float(lvl_ch_ed), float(rise_coeff), float(power),
                          float(speed), float(wisdom), float(intellect), float(endurance), float(attack_coeff),
                          float(defence_coeff), float(hp_coeff), float(mana_coeff))
        f.close()
        return hero

    @staticmethod
    def monster(monster_name):

        monsters = {
            'Chupakabra': Monsters.Chupakabra
        }

        for line in open('Code/SavingData/monsters.txt', 'r'):
            name, lvl = line.split()
            if name == monster_name:
                return monsters[monster_name](int(lvl))


class PassData:

    def __init__(self):
        pass

    @staticmethod
    def main_hero(hero):
        f = open('Code/SavingData/main_hero.txt', 'w')
        line = str(hero.name) + " "
        line += str(hero.lvl) + " "
        line += str(hero.gold) + " "
        line += str(hero.exp) + " "
        line += str(hero.lvl_changing_edge) + " "
        line += str(hero.rise_coeff) + " "
        line += str(hero.power) + " "
        line += str(hero.speed) + " "
        line += str(hero.wisdom) + " "
        line += str(hero.intellect) + " "
        line += str(hero.endurance) + " "
        line += str(hero.attack_coeff) + " "
        line += str(hero.defence_coeff) + " "
        line += str(hero.hp_coeff) + " "
        line += str(hero.mana_coeff) + " "
        f.seek(0)
        f.write(line)
        f.close()






