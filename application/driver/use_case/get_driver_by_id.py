from domain.driver.interface import DriverRepository


class GetDriverById:
    storage: DriverRepository

    def __init__(self, storage: DriverRepository) -> None:
        self.storage = storage

    def execute(self, driver_id: int):
        return self.storage.get_by_id(driver_id)
