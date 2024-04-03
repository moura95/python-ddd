from application.driver.driver_schema import DriverSchema
from domain.driver.interface import DriverRepository


class GetAllDrivers:
    storage: DriverRepository

    def __init__(self, storage: DriverRepository) -> None:
        self.storage = storage

    def execute(self, user_dto: DriverSchema):
        return self.storage.get_all()
