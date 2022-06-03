from Code.BasicFuncs.Game.Warehouse.Equipping import Choose
from Code.Classes.Equipment.PotionsService import PotionsLinks
from Code.Classes.Equipment.ArmorService import ArmorLinks
from Code.Classes.Equipment.ArtefactsService import ArtefactsLinks


def put_it_off(_id):

    if _id in PotionsLinks.potions_id:
        Choose.potion_off(_id)

    if _id in ArtefactsLinks.artefacts_id:
        Choose.artefact_off(_id)

    if _id in ArmorLinks.armors_id:
        Choose.armor_off(_id)


def put_it_on(_id):

    if _id in PotionsLinks.potions_id:
        Choose.take_potion(_id)

    if _id in ArtefactsLinks.artefacts_id:
        Choose.take_artefact(_id)

    if _id in ArmorLinks.armors_id:
        Choose.take_armor(_id)