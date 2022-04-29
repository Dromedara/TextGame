import Code.ArtefactsServices.CreateArtefact as CreateArtefact
import Code.PotionsServices.CreatePotion as CreatePotion
import random


def create_artefacts(lvl):

    staff = {}
    for key in CreateArtefact.artefacts_dict.keys():
        staff[key] = CreateArtefact.Creator.create_artefact(key=key, rarity=random.randrange(1, lvl + 1, 1))

    return staff


def create_potions(lvl):
    staff = {}
    for key in CreatePotion.potions_dict.keys():
        staff[key] = CreatePotion.Creator.create_potion(key=key, rarity=random.randrange(1, lvl + 1, 1))

    return staff
