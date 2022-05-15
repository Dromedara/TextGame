class InventoryChecker:

    @staticmethod
    def add(obj_dict, obj):
        if obj_dict.get(obj) is None:
            obj_dict[obj] = []
        return obj_dict
