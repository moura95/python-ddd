from domain.driver.interface import DriverRepository


class DeleteDriverUseCase:
    storage: DriverRepository

    def __init__(self, storage: DriverRepository) -> None:
        self.storage = storage

    def execute(self, driver_id: int):
        try:
            driver = self.storage.get_by_id(driver_id)
            self.storage.delete(driver.id)
            return {'message': 'Delete Success', 'code': 200}
        except Exception as e:
            return {'message': "Delete Failed", 'code': 500}
