from abc import ABC, abstractclassmethod

from application.vehicle.vehicle_schema import VehicleSchema


class VehicleRepository(ABC):

    @classmethod
    def save(self, bookingDto: VehicleSchema):
        pass

    @classmethod
    def get_all(self):
        pass

    @classmethod
    def get_by_id(self, id) -> VehicleSchema:
        pass

    @classmethod
    def update(self, booking_dto: VehicleSchema):
        pass

    @classmethod
    def delete(self, booking_dto: VehicleSchema):
        pass
