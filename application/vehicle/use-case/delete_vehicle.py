from domain.vehicle.interface import VehicleRepository


class DeleteVehicleUseCase:
    storage: VehicleRepository

    def __init__(self, storage: VehicleRepository) -> None:
        self.storage = storage

    def execute(self, vehicle_id: int):
        try:
            vehicle = self.storage.get_by_id(vehicle_id)
            if vehicle:
                self.storage.delete(vehicle.id)
                return {'message': 'Delete Success', 'code': 200}
            return {"message": 'Not Found', 'code': 200}
        except Exception as e:
            return {'message': "Delete Failed", 'code': 500}
