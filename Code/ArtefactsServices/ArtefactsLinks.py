import Code.ArtefactsServices.Artefact

artefact_battle_slots = {
            'armor': '',
            'sword': '',
            'amulet': ''
        }

armors = ['simple_iron_armor', 'simple_iron_armor']

swords = ['simple_sword', 'charmed_sword']

amulets = ['simple_amulet', 'super_amulet']

active_artefact_dict = {
    'straight_sword_attack': Code.ArtefactsServices.Artefact.SimpleSword.straight_sword_attack,
    'forced_sword_attack': Code.ArtefactsServices.Artefact.CharmedSword.forced_sword_attack,
    'charmed_sword_attack': Code.ArtefactsServices.Artefact.CharmedSword.charmed_sword_attack,
    'super_magic_attack': Code.ArtefactsServices.Artefact.SuperMagicAmulet.super_magic_attack
}


passive_artefact_dict = {
    'simple_passive_attack': Code.ArtefactsServices.Artefact.CharmedIronArmor.simple_passive_attack,
    'simple_magic_baff': Code.ArtefactsServices.Artefact.SimpleMagicAmulet.simple_magic_baff,
    'super_magic_baff': Code.ArtefactsServices.Artefact.SuperMagicAmulet.super_magic_baff
}