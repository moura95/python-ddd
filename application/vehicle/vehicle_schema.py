from pydantic import BaseModel

from domain.vehicle.entity import Vehicle


class VehicleSchema(BaseModel):
    brand: str
    model: str
    license_plate: str
    color: str | None

    def to_domain(self) -> Vehicle:
        vehicle = Vehicle(brand=self.brand, model=self.model, license_plate=self.license_plate, color=self.color)
        return vehicle

    @staticmethod
    def to_dto(vehicle: Vehicle):
        vehicle_schema = VehicleSchema(brand=vehicle.brand, model=vehicle.model, license_plate=vehicle.license_plate, color=vehicle.color)
        return vehicle_schema
