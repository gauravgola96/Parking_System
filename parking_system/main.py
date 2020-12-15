from parking_system.parking_system import ParkingSystem
from parking_system.driver import Driver
from parking_system.vehicles import Car
from parking_system import current_config
import logging

logger = logging.getLogger(__name__)


class RunParkingSystem:
    """
    Perform operation on the basis of command input:

    'Create_parking_lot': case_1(),
    'Park': case_2(),
    'Leave': case_3(),
    'Vehicle_registration_number_for_driver_of_age': case_4(),
    'Slot_numbers_for_driver_of_age': case_5(),
    'Slot_number_for_car_with_number': case_6()
    """

    def __init__(self):
        self.obj = None

    def run(self, command: str, **kwargs):
        """
        :param command: User input command in string
        :param kwargs: params for specific method
        :return:
        """
        default = "Invalid input command"
        try:
            case_no = current_config.COMMAND_DICT[command]
        except KeyError:
            logger.info(default)
            return
        return getattr(self, 'case_' + str(case_no), lambda: default)(**kwargs)

    def case_1(self, **kwargs):
        """Create_parking_lot"""
        if 'slots' in kwargs:
            self.obj = ParkingSystem(slots=int(kwargs['slots']))
            return
        logger.debug(" Invalid arguments: Argument slots is required")
        return

    def case_2(self, **kwargs):
        """Park"""
        if 'reg_no' in kwargs and 'age' in kwargs:
            if isinstance(self.obj, ParkingSystem):
                car = Car(registration_number=kwargs['reg_no'])
                driver = Driver(age=int(kwargs['age']))
                return self.obj.park_vehicle(car, driver)
            else:
                logger.debug("ParkingSystem instance is not yet created")
                return
        logger.debug(" Invalid arguments: Argument reg_no and age are required")
        return

    def case_3(self, **kwargs):
        """Leave"""
        if 'slot_no' in kwargs:
            if isinstance(self.obj, ParkingSystem):
                return self.obj.vacate_slot(slot_no=int(kwargs['slot_no']))
            else:
                logger.debug("ParkingSystem instance is not yet created")
                return
        logger.debug(" Invalid arguments: Argument slot is required")
        return

    def case_4(self, **kwargs):
        """Vehicle_registration_number_for_driver_of_age"""
        if 'age' in kwargs:
            if isinstance(self.obj, ParkingSystem):
                return self.obj.get_reg_from_age(age=int(kwargs['age']))
            else:
                logger.debug("ParkingSystem instance is not yet created")
                return
        logger.debug(" Invalid arguments: Argument age is required")
        return

    def case_5(self, **kwargs):
        """Slot_numbers_for_driver_of_age"""
        if 'age' in kwargs:
            if isinstance(self.obj, ParkingSystem):
                return self.obj.get_slots_from_age(age=int(kwargs['age']))
            else:
                logger.debug("ParkingSystem instance is not yet created")
                return
        logger.debug(" Invalid arguments: Argument age is required")
        return

    def case_6(self, **kwargs):
        """Slot_number_for_car_with_number"""
        if 'reg_no' in kwargs:
            if isinstance(self.obj, ParkingSystem):
                return self.obj.get_slot_from_reg(reg_no=kwargs['reg_no'])
            else:
                logger.debug("ParkingSystem instance is not yet created")
                return
        logger.debug(" Invalid arguments: Argument reg_no is required")
        return
