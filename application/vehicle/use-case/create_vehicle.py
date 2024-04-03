from application.vehicle.vehicle_schema import VehicleSchema
from domain.vehicle.interface import VehicleRepository


class CreateVehicleUseCase:
    storage: VehicleRepository

    def __init__(self, storage: VehicleRepository) -> None:
        self.storage = storage

    def execute(self, vehicle_schema: VehicleSchema):
        try:
            vehicle = vehicle_schema.to_domain()
            valid = vehicle.is_valid()
            if not valid:
                return {'message': 'Vehicle is not valid', 'code': 400}

            self.storage.save(vehicle_schema)
            return {'message': "Success Create Vehicle", 'code': 201}
        except Exception as e:
            return {'message': 'ErrorCodes.UNDEFINED.value', 'code': 'ErrorCodes.UNDEFINED.name'}
