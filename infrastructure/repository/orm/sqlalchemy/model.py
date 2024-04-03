from datetime import datetime

from sqlalchemy import func, Column, ForeignKey, Integer
from sqlalchemy.orm import mapped_column, Mapped, relationship

from infrastructure.database.base_model import Base


class DriverVehicle(Base):
    __tablename__ = "core_drivers_vehicles"

    vehicle_id = Column(Integer, ForeignKey('core_vehicles.id'), primary_key=True)
    driver_id = Column(Integer, ForeignKey('core_drivers.id'), primary_key=True)
    driver = relationship("Driver", back_populates="vehicles")
    vehicle = relationship("Vehicle", back_populates="drivers")


class Driver(Base):
    __tablename__ = "core_drivers"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    email: Mapped[str]
    tax_id: Mapped[str]
    driver_license: Mapped[str]
    date_of_birth: Mapped[datetime]
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(),
                                                 onupdate=func.now())


class Vehicle(Base):
    __tablename__ = "core_vehicles"

    id: Mapped[int] = mapped_column(primary_key=True)
    model: Mapped[str]
    license_plate: Mapped[str]
    color: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(),
                                                 onupdate=func.now())
