class Utils:

    @staticmethod
    def get_reg_no(reg_slot_dict: dict, slot: int) -> str or None:
        """Get key from value"""
        for key, value in reg_slot_dict.items():
            if slot == value:
                return key
        return None

    @staticmethod
    def get_age_from_reg(age_reg_dict: dict, reg_no: str) -> int or None:
        """Get key from value"""
        for age, reg_list in age_reg_dict.items():
            if reg_no in reg_list: return age
        return None

    @staticmethod
    def get_age_from_slot(age_slot_dict: dict, slot_no: int) -> int or None:
        """Get key from value"""
        for age, slot_list in age_slot_dict.items():
            if slot_no in slot_list: return age
        return None
