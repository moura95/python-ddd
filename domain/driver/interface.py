from abc import ABC, abstractclassmethod
from driver_schema import DriverSchema


class DriverRepository(ABC):

    @classmethod
    def save(self, driverDTO: DriverSchema):
        pass

    @classmethod
    def get_all(self):
        pass

    @classmethod
    def get_by_id(self, id) -> DriverSchema:
        pass

    @classmethod
    def update(self, driverDTO: DriverSchema):
        pass

    @classmethod
    def delete(self, driverDTO: DriverSchema):
        pass
