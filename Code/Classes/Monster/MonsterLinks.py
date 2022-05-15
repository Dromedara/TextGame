from Code.Classes.Monster import Monsters

monsters_creator_dict = {
            'Chupakabra': Monsters.Chupakabra
        }

active_skills_dict = {
    'strait_physical_attack': Monsters.Chupakabra.strait_physical_attack,
    'straight_magic_attack': Monsters.Chupakabra.straight_magic_attack
}

passive_skills_dict = {
    'healing_itself': Monsters.Chupakabra.healing_itself
}
