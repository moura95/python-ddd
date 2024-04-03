from application.driver.driver_schema import DriverSchema
from domain.driver.interface import DriverRepository


class CreateDriverUseCase:
    storage: DriverRepository

    def __init__(self, storage: DriverRepository) -> None:
        self.storage = storage

    def execute(self, driver_schema: DriverSchema):
        try:
            driver = driver_schema.to_domain()
            valid = driver.is_valid()
            if not valid:
                return {'message': 'Driver is not valid', 'code': 400}

            self.storage.save(driver_schema)
            return {'message': "Success Create Driver", 'code': 201}
        except Exception as e:
            return {'message': 'ErrorCodes.UNDEFINED.value', 'code': 'ErrorCodes.UNDEFINED.name'}
