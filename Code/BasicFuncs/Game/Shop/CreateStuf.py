import COde_1.Classes.Equipment.ArmorService.ArmorLinks as ArmorLinks
import COde_1.Classes.Equipment.ArtefactsService.ArtefactsLinks as ArtefactsLinks
import COde_1.Classes.Equipment.PotionsService.PotionsLinks as PotionsLinks

from COde_1.Classes.Equipment.ArmorService.CreateArmor import ArmorCreator
from COde_1.Classes.Equipment.PotionsService.CreatePotions import PotionsCreator
from COde_1.Classes.Equipment.ArtefactsService.CreateArtefact import ArtefactCreator


def start_shop():
    selling_artefacts = {}
    for artefact in ArtefactsLinks.artefacts_list:
        a = ArtefactCreator.create_artefact(key=artefact)
        selling_artefacts[a.id] = a

    selling_potions = {}
    for potion in PotionsLinks.potions_list:
        p = PotionsCreator.create_potion(key=potion)
        selling_potions[p.id] = p

    selling_armors = {
        'helmet': {},
        'bib': {},
        'pants': {}
    }

    for helmet in ArmorLinks.helmet_list:
        h = ArmorCreator.create_armor(key=helmet)
        selling_armors['helmet'][h.id] = h

    for bib in ArmorLinks.bib_list:
        b = ArmorCreator.create_armor(key=bib)
        selling_armors['bib'][b.id] = b

    for pant in ArmorLinks.pants_list:
        p = ArmorCreator.create_armor(key=pant)
        selling_armors['pants'][p.id] = p

    return selling_artefacts, selling_armors, selling_potions


def armor_shop(selling_armors):

    print(selling_armors)

    for key in selling_armors['helmet'].keys():
        if selling_armors['helmet'][key] is None:
            selling_armors['helmet'][key] = ArmorLinks.creator_dict[key]()

    for key in selling_armors['bib'].keys():
        if selling_armors['bib'][key] is None:
            selling_armors['bib'][key] = ArmorLinks.creator_dict[key]()

    for key in selling_armors['pants'].keys():
        if selling_armors['pants'][key] is None:
            selling_armors['pants'][key] = ArmorLinks.creator_dict[key]()

    return selling_armors


def artefacts_shop(selling_artefacts):

    for key in selling_artefacts.keys():
        if selling_artefacts[key] is None:
            selling_artefacts[key] = ArtefactsLinks.creator_dict[key]()

    return selling_artefacts


def potions_shop(selling_potions):

    for key in selling_potions.keys():
        if selling_potions[key] is None:
            selling_potions[key] = PotionsLinks.potions_creator[key]()

    return selling_potions
