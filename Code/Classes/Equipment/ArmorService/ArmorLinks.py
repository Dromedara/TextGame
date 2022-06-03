import Code.Classes.Equipment.ArmorService.Armor as Armor

parts_dict = {
    'helmet': ['simple_helmet', 'super_helmet'],
    'bib': ['simple_bib', 'charmed_bib'],
    'pants': ['simple_pants']
}

armors_id = []

passive_armor_dict = {
    'simple_passive_attack': Armor.CharmedBib.simple_passive_attack
}

creator_dict = {
    'simple_helmet': Armor.SimpleHelmet,
    'super_helmet': Armor.SuperHelmet,
    'simple_bib': Armor.SimpleBib,
    'charmed_bib': Armor.CharmedBib,
    'simple_pants': Armor.SimplePants
}
