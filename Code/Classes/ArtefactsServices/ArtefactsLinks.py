import Code.Classes.ArtefactsServices.Artefacts.Amulets
import Code.Classes.ArtefactsServices.Artefacts.Armors
import Code.Classes.ArtefactsServices.Artefacts.Swords


artefact_battle_slots = {
            'armor': None,
            'sword': None,
            'amulets': []
        }

armors = ['simple_iron_armor', 'simple_iron_armor']

swords = ['simple_sword', 'charmed_sword']

amulets = ['simple_amulet', 'super_amulet']

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
