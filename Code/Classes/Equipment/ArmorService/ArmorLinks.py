import Code.Classes.Equipment.ArmorService.Armor as Armor

helmet_list = ['simple_helmet', 'super_helmet']
bib_list = ['simple_bib', 'charmed_bib']
pants_list = ['simple_pants']

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

id_counter = 0
