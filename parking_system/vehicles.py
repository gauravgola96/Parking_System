from abc import ABC
from enum import Enum
from parking_system.constants import VehicleType


class Vehicle(ABC):
    """Vehicle Base class"""
    def __init__(self, registration_number: str, vehicle_type: Enum):
        """

        :param registration_number: Vehicle registration number
        :param vehicle_type: Type of vehicle (car, truck, bus etc)
        """
        self.registration_number = registration_number
        self.vehicle_type = vehicle_type  # for extending on the basis of type of vehicles


class Car(Vehicle):
    def __init__(self, registration_number: str):
        super().__init__(registration_number, VehicleType.CAR)
