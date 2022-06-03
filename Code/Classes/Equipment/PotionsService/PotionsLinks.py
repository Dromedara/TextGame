import Code.Classes.Equipment.PotionsService.Potions as Potions

potions_list = ['protecting_potion', 'boosting_potion', 'healing_potion']

potions_baffs_dict = {
    'super_protector': Potions.ProtectingPotion.super_protector
}

potions_id = []

potions_creator = {
            'healing_potion': Potions.HealingPotion,
            'boosting_potion': Potions.BoostingPotion,
            'protecting_potion': Potions.ProtectingPotion
        }

