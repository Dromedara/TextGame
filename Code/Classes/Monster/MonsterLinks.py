from Code.Classes.Monster.MonsterTypes import Human
from Code.Classes.Monster.MonsterTypes import Beasts
from Code.Classes.Monster.MonsterTypes import Relic
from Code.Classes.Monster.MonsterTypes import Undead

'''Links for operations with monsters
'''

monsters_creator_dict = {
    'Thief': Human.Thief,
    'wild_dog': Beasts.WildDog
}

active_list = ['bite_attack']
passive_list = []

active_skills_dict = {
    'bite_attack': Beasts.WildDog.bite_attack,
}

passive_skills_dict = {}
