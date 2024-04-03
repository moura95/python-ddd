from domain.vehicle.interface import VehicleRepository


class VehicleService:
    storage: VehicleRepository

    def __init__(self, storage: VehicleRepository) -> None:
        self.storage = storage

    def execute(self, vehicle_id: int):
        return self.storage.get_by_id(vehicle_id)
