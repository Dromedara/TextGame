import Code.Classes.Equipment.ArmorService.ArmorLinks as ArmorLinks
import Code.Classes.Equipment.ArtefactsService.ArtefactsLinks as ArtefactsLinks
import Code.Classes.Equipment.PotionsService.PotionsLinks as PotionsLinks

from Code.Classes.Equipment.ArmorService.CreateArmor import ArmorCreator
from Code.Classes.Equipment.PotionsService.CreatePotions import PotionsCreator
from Code.Classes.Equipment.ArtefactsService.CreateArtefact import ArtefactCreator


def start_shop():

    selling_artefacts = {}
    for artefact in ArtefactsLinks.artefacts_list:
        a = ArtefactCreator.create_artefact(key=artefact)
        selling_artefacts[a.id] = a

    selling_potions = {}
    for potion in PotionsLinks.potions_list:
        p = PotionsCreator.create_potion(key=potion)
        selling_potions[p.id] = p

    selling_armors = {}
    for key in ArmorLinks.parts_dict.keys():
        selling_armors[key] = {}

    for part in ArmorLinks.parts_dict.keys():
        for key in ArmorLinks.parts_dict[part]:
            a = ArmorCreator.create_armor(key=key)
            selling_armors[part][a.id] = a

    return selling_artefacts, selling_armors, selling_potions


def armor_shop(keyword, part, selling_armors):

    a = ArmorCreator.create_armor(key=keyword)
    selling_armors[part][a.id] = a

    return selling_armors


def artefacts_shop(keyword, selling_artefacts):

    a = ArtefactCreator.create_artefact(key=keyword)

    selling_artefacts[a.id] = a

    return selling_artefacts


def potions_shop(keyword, selling_potions):

    p = PotionsCreator.create_potion(key=keyword)
    selling_potions[p.id] = p

    return selling_potions
