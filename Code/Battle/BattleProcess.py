import Code.Battle.Preparing as Preparing
import Code.Classes.AdventurerSkills as AdventurerSkills
import Code.Classes.MonsterSkills as MonsterSkills
import random
import Code.Checking.SOS as SOS
from Code.Checking.Attention import AttentionMessages


def end(hero):
    if hero.hp <= 0:
        SOS.SOSMessages.lose_battle()
        return 'lose'

    AttentionMessages.win()
    return 'win'


def show(hero):
    print(hero.hero_active_skills)
    print(hero.hero_passive_skills)
    print(f"hp: {hero.hp},\nattack: {hero.attack},\ndefence: {hero.defence},\nmana: {hero.mana},\nmagic attack: {hero.magic_attack}\n")


def check(hero, monster):
    if hero.hp <= 0 or monster.hp <= 0:
        return True
    return False


def Battle(hero, adventure):

    hero = Preparing.prepare_hero(hero)

    monster = Preparing.prepare_monster(adventure)

    hero_actives_activator = AdventurerSkills.ActiveSkills()
    hero_passives_activator = AdventurerSkills.PassiveSkills()
    
    monster_actives_activator = MonsterSkills.ActiveSkills()
    monster_passives_activator = MonsterSkills.PassiveSkills()

    hero_actives = {
        'straight_sword_attack': hero_actives_activator.straight_sword_attack,
        'forced_sword_attack': hero_actives_activator.forced_sword_attack,
        'super_magic_attack': hero_actives_activator.super_magic_attack,
        'charmed_sword_attack': hero_actives_activator.charmed_sword_attack
    }

    hero_passives = {
        'passive_magic_attack': hero_passives_activator.passive_magic_attack,
        'simple_magic_baff': hero_passives_activator.simple_magic_baff
    }
    
    monster_actives = {
        1: monster_actives_activator.strait_physical_attack,
        2: monster_actives_activator.straight_magic_attack
    }
    
    monster_passives = {
        'healing_itself': monster_passives_activator.healing_itself
    }

    AttentionMessages.battle_start()
    while True:

        AttentionMessages.your_step()
        # hero
        
        for key in hero_passives.keys():
            hero_passives[key](hero, monster)
    
        show(hero)
        
        action = input()
        hero, monster = hero_actives[action](hero, monster)

        if check(hero, monster):
            break

        AttentionMessages.monster_step()
        # monster
        
        for key in monster_passives.keys():
            monster_passives[key](hero, monster)
            
        action = random.randrange(1, 2, 1)

        print(f" actijon: {action}")
        
        hero, monster = monster_actives[action](hero, monster)

        if check(hero, monster):
            break

    AttentionMessages.battle_end()

    return end(hero)
