from application.vehicle.vehicle_schema import VehicleSchema
from domain.vehicle.interface import VehicleRepository


class VehicleService:
    storage: VehicleRepository

    def __init__(self, storage: VehicleRepository) -> None:
        self.storage = storage

    def execute(self):
        return self.storage.get_all()
