import logging
from parking_system import current_config

logger = logging.getLogger(__name__)


class Helper:
    """Input string verification"""

    @staticmethod
    def fetch_required_param_name(cmd):
        """Checks command string and returns its required parameter name required to run its method"""
        try:
            case_no = current_config.COMMAND_DICT[cmd]
            if case_no == 1:
                """Create_parking_lot"""
                return ["slots"]
            elif case_no == 2:
                """Park"""
                return ["reg_no", "age"]
            elif case_no == 3:
                """ Leave """
                return ["slot_no"]
            elif case_no == 4:
                """Vehicle_registration_number_for_driver_of_age"""
                return ["age"]
            elif case_no == 5:
                """Slot_numbers_for_driver_of_age"""
                return ["age"]
            elif case_no == 6:
                """Slot_number_for_car_with_number"""
                return ["reg_no"]
        except KeyError:
            return
            # logger.debug("Something wrong with input")
            # raise InvalidParams("Something wrong with input")

    @staticmethod
    def fetch_input_values(cmd, params):
        """Checks command string and returns parameter values required to run its method. \
            User input values like reg_no, age, slots"""
        try:
            case_no = current_config.COMMAND_DICT[cmd]
            if case_no == 1:
                """Create_parking_lot"""
                if len(params) == 1:
                    return [params[0]]

            elif case_no == 2:
                """Park"""
                if len(params) == 3:
                    return [params[0], params[2]]

            elif case_no == 3:
                """ Leave """
                if len(params) == 1:
                    return [params[0]]
                logger.debug("Something wrong with input")

            elif case_no == 4:
                """Vehicle_registration_number_for_driver_of_age"""
                if len(params) == 1:
                    return [params[0]]

            elif case_no == 5:
                """Slot_numbers_for_driver_of_age"""
                if len(params) == 1:
                    return [params[0]]

            elif case_no == 6:
                """Slot_number_for_car_with_number"""
                if len(params) == 1:
                    return [params[0]]

        except KeyError:
            return
            # logger.debug("Something wrong with input")
            # raise InvalidParams("Something wrong with input")
