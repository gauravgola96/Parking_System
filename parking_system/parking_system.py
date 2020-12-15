import logging
from heapq import heappush, heappop
from parking_system.utils import Utils
from collections import defaultdict

logger = logging.getLogger(__name__)


class ParkingSystem:
    """
    Singleton design pattern Only a single instance of ParkingSystem will be available in the system. If new instance
    is recreated it will updated (on same address) with new number of slots and empty mappings.
    """
    _instance = None

    def __new__(cls, slots, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ParkingSystem, cls).__new__(
                cls, *args, **kwargs)
        else:
            logger.debug(f"Recreated parking lot with capacity :{slots}")
        return cls._instance

    def __init__(self, slots: int, *args, **kwargs):
        """
        Initialize mappings and fill the slots with min-heap

        :param slots: Number of slots for parking system
        """
        super().__init__(*args, **kwargs)
        self.slots = slots
        self.registration_slot_mapping = dict()
        self.age_slot_mapping = defaultdict(list)
        # self.age_registration_mapping = defaultdict(list)
        self.available_slots = []

        for i in range(1, self.slots + 1):
            heappush(self.available_slots, i)
        logger.info(f"Created parking of {slots} slots")

    def __str__(self):
        return f"ParkingSystem with {self.slots} slots"

    def nearest_available_slot(self) -> int or None:
        """Gets the nearest available slot"""
        if self.available_slots:
            return heappop(self.available_slots)
        else:
            return None

    def park_vehicle(self, vehicle, driver) -> None:
        """
        Park vehicle in the nearest available slot and update the required mappings
        :param vehicle: vehicle instance
        :param driver: Driver instance
        :return:
        """
        slot_no = self.nearest_available_slot()

        if slot_no is None:
            logger.info("All parking slots are occupied !!")
            return None

        self.registration_slot_mapping[vehicle.registration_number] = slot_no
        # self.age_registration_mapping[driver.age].append(vehicle.registration_number)
        self.age_slot_mapping[driver.age].append(slot_no)
        logger.info(f'Car with vehicle registration number "{vehicle.registration_number}" has been parked at slot '
                    f'number {slot_no}')
        return None

    def vacate_slot(self, slot_no: int) -> None:
        """
        Vacate the requested slot, update the respective mappings and update avaible slots with min-heap
        :param slot_no: Slot to be vacate
        :return:
        """
        if slot_no in self.registration_slot_mapping.values():
            reg_no = Utils.get_reg_no(self.registration_slot_mapping, slot_no)
            del self.registration_slot_mapping[reg_no]
            driver_age = Utils.get_age_from_slot(self.age_slot_mapping, slot_no)
            # driver_age = Utils.get_age_from_reg(self.age_registration_mapping, reg_no)
            self.age_slot_mapping[driver_age].remove(slot_no)
            # self.age_registration_mapping[driver_age].remove(reg_no)

            heappush(self.available_slots, slot_no)
            logger.info(f'Slot number {slot_no} vacated, the car with vehicle registration number "{reg_no}" left the '
                        f'space, the driver of the car was of age {driver_age}')
            return None
        elif (slot_no > self.slots) or (slot_no < 1):
            logger.info(f"Slot {slot_no} doesn't exist")
            return None
        else:
            logger.info("Slot already vacant")
            return None

    def get_slots_from_age(self, age: int) -> None:
        """
        Get slots assinged to the requested age
        :param age: Driver age
        :return:
        """
        slot_list = self.age_slot_mapping[age]
        if slot_list:
            logger.info(str(slot_list)[1:-1])
        else:
            logger.info("null")
        return None

    def get_reg_from_age(self, age: int) -> None:
        """
        Get registration number of the cars assigned to the requested age
        :param age: Driver age
        :return:
        """
        slot_list = self.age_slot_mapping[age]
        if slot_list:
            reg_list = [Utils.get_reg_no(self.registration_slot_mapping, slot) for slot in slot_list]
            # reg_list = self.age_registration_mapping[age]
            logger.info(str(reg_list)[1:-1])
        else:
            logger.info("null")
        return None

    def get_slot_from_reg(self, reg_no: str) -> None:
        """
        Get slot assigned to requested registration number
        :param reg_no: Vehicle registration number
        :return:
        """
        try:
            slot_no = self.registration_slot_mapping[reg_no]
            logger.info(str(slot_no))
        except KeyError:
            logger.info("null")
        return
