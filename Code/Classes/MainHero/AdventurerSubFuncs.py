class AdventurerChecker:
    """Checker of different technical aspects of adventurer skills functions.

    """

    @staticmethod
    def exp_change(param, edge):
        """Check if there is more exp points needed for raising lvl.

        :param param: 
        :param edge:
        :return:
        """
        if param < edge:
            return False
        return True
