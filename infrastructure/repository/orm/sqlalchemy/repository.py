import sys

from application.driver.driver_schema import DriverSchema
from application.vehicle.vehicle_schema import VehicleSchema

# sys.path.append('../../..')
# sys.path.append('../../../..')
from domain.driver.interface import DriverRepository
from domain.vehicle.interface import VehicleRepository
from infrastructure.database import db
from infrastructure.repository.orm.sqlalchemy.model import Driver, Vehicle


class DriverRepositorySqlAlchemy(DriverRepository):
    def __init__(self):
        self.db = db

    def save(self, driverSchema: DriverSchema):
        new = Driver(
            name=driverSchema.name, email=driverSchema.email, tax_id=driverSchema.tax_id,
            driver_license=driverSchema.driver_license, date_of_birth=driverSchema.date_of_birth)
        db.session.add(new)
        db.session.commit()
        db.session.flush()

    def get_by_id(self, id) -> DriverSchema:
        driver = Driver.query.get(id)
        return self._model_to_dto(driver)

    def update(self, driver_dto: DriverSchema):
        pass

    def delete(self, driver_dto: DriverSchema):
        Driver.query.get(driver_dto.id)
        db.session.commit()

    def _model_to_dto(self, driver: Driver):
        customer_dto = DriverSchema(name=driver.name, email=driver.email, tax_id=driver.tax_id,
                                    driver_license=driver.driver_license, date_of_birth=driver.date_of_birth)
        return customer_dto

    def get_all(self):
        drivers = Driver.query.all()
        drivers_dto = []
        for d in drivers:
            driver = Driver.query.filter_by(id=d.id).first()
            drivers_dto.append(self._model_to_dto(driver))
        return drivers_dto


class VehicleRepositorySqlAlchemy(VehicleRepository):
    def __init__(self):
        self.db = db

    def save(self, vehicleSchema: VehicleSchema):
        new = Vehicle(
            brand=vehicleSchema.brand, model=vehicleSchema.model, license_plate=vehicleSchema.license_plate,
            color=vehicleSchema.color)
        db.session.add(new)
        db.session.commit()
        db.session.flush()

    def get_by_id(self, id) -> VehicleSchema:
        vehicle = Vehicle.query.get(id)
        return self._model_to_dto(vehicle)

    def update(self, vehicle_dto: VehicleSchema):
        pass

    def delete(self, vehicle_dto: VehicleSchema):
        vehicle = Vehicle.query.get(vehicle_dto.id)
        db.session.commit()

    def _model_to_dto(self, vehicleSchema: VehicleSchema):
        vehicle_dto = VehicleSchema(brand=vehicleSchema.brand, model=vehicleSchema.model,
                                    license_plate=vehicleSchema.license_plate,
                                    color=vehicleSchema.color)
        return vehicle_dto

    def get_all(self):
        vehicles = Vehicle.query.all()
        vehicles_dto = []
        for v in vehicles:
            vehicle = Vehicle.query.filter_by(id=v.id).first()
            vehicles_dto.append(self._model_to_dto(vehicle))
        return vehicles_dto
