from typing import List

from .exception import *
from datetime import datetime

from ..vehicle.entity import Vehicle


class Driver:
    name: str
    email: str
    tax_id: str
    driver_license: str
    date_of_birth: datetime
    vehicles: List[Vehicle]

    def __init__(self, name: str, email: str, tax_id: str, driver_license: str, date_of_birth: datetime):
        self.name = name
        self.email = email
        self.tax_id = tax_id
        self.driver_license = driver_license
        self.date_of_birth = date_of_birth

    def is_valid(self):
        if not self.name:
            raise NameCannotBeEmpty("Name cannot be empty")
        if not self.email:
            raise EmailCannotBeEmpty("Email cannot be empty")
        # Add more validations as needed
        return True
