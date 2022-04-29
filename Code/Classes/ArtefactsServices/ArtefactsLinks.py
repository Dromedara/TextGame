import Code.Classes.ArtefactsServices

all_artefacts = []

curr_artefacts = {
    'armor': None,
    'sword': None,
    'amulet': None
}

active_artefact_dict = {
    'straight_sword_attack': Code.Classes.ArtefactsServices.Artefacts.Swords.SimpleSword.straight_sword_attack,
    'forced_sword_attack': Code.Classes.ArtefactsServices.Artefacts.Swords.CharmedSword.forced_sword_attack,
    'charmed_sword_attack': Code.Classes.ArtefactsServices.Artefacts.Swords.CharmedSword.charmed_sword_attack,
    'super_magic_attack': Code.Classes.ArtefactsServices.Artefacts.Amulets.SuperMagicAmulet.super_magic_attack
}


passive_artefact_dict = {
    'simple_passive_attack': Code.Classes.ArtefactsServices.Artefacts.Armors.CharmedIronArmor.simple_passive_attack,
    'simple_magic_baff': Code.Classes.ArtefactsServices.Artefacts.Amulets.SimpleMagicAmulet.simple_magic_baff,
    'super_magic_baff': Code.Classes.ArtefactsServices.Artefacts.Amulets.SuperMagicAmulet.super_magic_baff
}