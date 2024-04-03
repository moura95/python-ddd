from application.driver.driver_schema import DriverSchema
from domain.driver.interface import DriverRepository


class UpdateDriver:
    storage: DriverRepository

    def __init__(self, storage: DriverRepository) -> None:
        self.storage = storage

    def execute(self, driver_schema: DriverSchema):
        try:
            driver_domain = driver_schema.to_domain()
            valid = driver_domain.is_valid()
            if not valid:
                return {'message': 'Invalid Driver', 'code': 400}
            self.storage.update(driver_schema)
            return {'message': 'Success Update Driver', 'code': 200}
        except Exception as e:
            return {'message': "Update Failed", 'code': 500}
