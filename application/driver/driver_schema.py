from datetime import datetime
from pydantic import BaseModel

from domain.driver.entity import Driver


class DriverSchema(BaseModel):
    name: str
    email: str
    tax_id: str
    driver_license: str | None
    date_of_birth: datetime | None

    def to_domain(self) -> Driver:
        driver = Driver(name=self.name, email=self.email, tax_id=self.tax_id, driver_license=self.driver_license,
                        date_of_birth=self.date_of_birth)
        driver.id = self.id
        driver.status = self.status
        return driver

    @staticmethod
    def to_schema(driver: Driver):
        driver_schema = DriverSchema(
            name=driver.name, email=driver.email, tax_id=driver.tax_id, driver_license=driver.driver_license,
            date_of_birth=driver.date_of_birth)
        return driver_schema
