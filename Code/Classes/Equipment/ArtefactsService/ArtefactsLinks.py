import Code.Classes.Equipment.ArtefactsService.Artefacts as Artefacts


artefacts_list = ['simple_amulet', 'super_amulet', 'simple_sword', 'charmed_sword']


active_artefact_dict = {
    'straight_sword_attack': Artefacts.SimpleSword.straight_sword_attack,
    'forced_sword_attack': Artefacts.CharmedSword.forced_sword_attack,
    'charmed_sword_attack': Artefacts.CharmedSword.charmed_sword_attack,
    'super_magic_attack': Artefacts.SuperMagicAmulet.super_magic_attack
}


passive_artefact_dict = {
    'simple_magic_baff': Artefacts.SimpleMagicAmulet.simple_magic_baff,
    'super_magic_baff': Artefacts.SuperMagicAmulet.super_magic_baff
}

creator_dict = {
        'simple_amulet': Artefacts.SimpleMagicAmulet,
        'super_amulet': Artefacts.SuperMagicAmulet,
        'simple_sword': Artefacts.SimpleSword,
        'charmed_sword': Artefacts.CharmedSword
}

id_counter = 4
