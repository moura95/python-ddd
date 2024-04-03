from datetime import datetime
from typing import List

from .exception import *
from ..driver.entity import Driver


class Vehicle:
    brand: str
    model: str
    license_plate: str
    color: str
    drivers: List[Driver]

    def __init__(self, brand: str, model: str, license_plate: str, color: str):
        self.brand = brand
        self.model = model
        self.license_plate = license_plate
        self.color = color

    def is_valid(self):
        if not self.brand:
            raise BrandCannotBeEmpty("Brand cannot be empty")
        if not self.model:
            raise ModelCannotBeEmpty("Model cannot be empty")
        # Add more validations as needed
        return True
