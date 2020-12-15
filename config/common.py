import logging


class Config:
    LOG_LEVEL = logging.DEBUG

    COMMAND_DICT = \
        {
            'Create_parking_lot': 1,
            'Park': 2,
            'Leave': 3,
            'Vehicle_registration_number_for_driver_of_age': 4,
            'Slot_numbers_for_driver_of_age': 5,
            'Slot_number_for_car_with_number': 6
        }
