import unittest
from datetime import datetime, timedelta
import sys
from application.driver.driver_schema import UserDto
from domain.driver.enum import BookingStatuses
sys.path.append('../booking_service')
sys.path.append('..')
from application.driver.driver_service import BookingManager
from application.driver.driver_schema import DriverSchema
from application.customers.customer_dto import CustomerDto
from domain.driver.interface import DriverRepository

class DummyStorage(DriverRepository):
    def save(self, driverDTO: DriverSchema):
        return True

    def get_by_id(self, id) -> DriverSchema:
        if id == 1:
            checkin = datetime.today()
            checkout = datetime.today()
            customer = CustomerDto("Customer", 18, "doc123", "a@a.com")
            booking_dto = DriverSchema(checkin=checkin, checkout=checkout, customer=customer)
            booking_dto.id = 1
            booking_dto.status = BookingStatuses.CANCELED.name
        else:
            checkin = datetime.today()
            checkout = datetime.today()
            customer = CustomerDto("Customer", 18, "doc123", "a@a.com")
            booking_dto = DriverSchema(checkin=checkin, checkout=checkout, customer=customer)
            booking_dto.id = 2
            booking_dto.status = BookingStatuses.RESERVED
        return booking_dto

    def update(self, booking_dto: DriverSchema):
        pass

    def get_all(self):
        checkin = datetime.today()
        checkout = datetime.today()
        customer = CustomerDto("Customer", 18, "doc123", "a@a.com")
        booking_dto1 = DriverSchema(checkin, checkout, customer)

        customer = CustomerDto("Customer", 18, "doc123", "a@a.com")
        booking_dto2 = DriverSchema(checkin, checkout, customer)
        admin_bookings = [booking_dto1, booking_dto2]
        return admin_bookings

    def get(self):
        checkin = datetime.today()
        checkout = datetime.today()
        customer = CustomerDto("Customer", 18, "doc123", "a@a.com")
        booking_dto1 = DriverSchema(checkin, checkout, customer)

        filtered_bookings = [booking_dto1]

        return filtered_bookings
    
    def delete(self, booking_dto: DriverSchema):
        pass

class BookingAggregateManagerTests(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        self.dummy_storage = DummyStorage()
        super().__init__(methodName)

    def test_get_all_bookings_admin(self):
        manager = BookingManager(self.dummy_storage)
        user_dto = UserDto('admin', True)
        bookings = manager.get_drivers(user_dto)
        self.assertEqual(len(bookings), 2)

    def test_get_all_bookings_non_admin(self):
        manager = BookingManager(self.dummy_storage)
        user_dto = UserDto('non_admin', False)
        user_dto.id = 1
        bookings = manager.get_drivers(user_dto)
        self.assertEqual(len(bookings), 1)

    def test_checkin_date_cannot_be_after_checkout(self):
        checkin = datetime.today()
        checkout = datetime.today() - timedelta(days=1)
        customer = CustomerDto("Customer", 18, "doc123", "a@a.com")
        booking_dto = DriverSchema(checkin=checkin, checkout=checkout, customer=customer)
        manager = BookingManager(self.dummy_storage)
        res = manager.create_new_booking(booking_dto)
        self.assertEqual(res['code'], 'CHECKINAFTERCHECKOUT')

    def test_customer_should_be_older_than_18(self):
        checkin = datetime.today()
        checkout = datetime.today()
        customer = CustomerDto("Customer", 17, "doc123", "a@a.com")
        booking_dto = DriverSchema(checkin=checkin, checkout=checkout, customer=customer)
        manager = BookingManager(self.dummy_storage)
        res = manager.create_new_booking(booking_dto)
        self.assertEqual(res['code'], 'CUSTOMERSHOULDBEOLDERTHAN18')

    def test_customer_document_should_be_valid(self):
        checkin = datetime.today()
        checkout = datetime.today()
        customer = CustomerDto("Customer", 18, "doc1", "a@a.com")
        booking_dto = DriverSchema(checkin=checkin, checkout=checkout, customer=customer)
        manager = BookingManager(self.dummy_storage)
        res = manager.create_new_booking(booking_dto)
        self.assertEqual(res['code'], 'INVALIDCUSTOMERDOCUMENT')

    def test_create(self):
        checkin = datetime.utcnow()
        checkout = datetime.today()
        customer = CustomerDto("Customer", 18, "doc123", "a@a.com")
        booking_dto = DriverSchema(checkin=checkin, checkout=checkout, customer=customer)
        manager = BookingManager(self.dummy_storage)
        res = manager.create_new_booking(booking_dto)
        self.assertEqual(res['code'], 'SUCCESS')

    def test_get_booking_by_id_admin_should_see_canceled_bookings(self):
        user_dto = UserDto('admin', True)
        manager = BookingManager(self.dummy_storage)
        res = manager.get_by_id(1, user_dto)
        self.assertEqual(res['code'], 'SUCCESS')
    
    def test_get_booking_by_id_non_admin_should_not_see_canceled_bookings(self):
        user_dto = UserDto('non_admin', False)
        manager = BookingManager(self.dummy_storage)
        res = manager.get_by_id(1, user_dto)
        self.assertEqual(res['code'], 'USERNOTALLOWEDTOACCESSDATA')

    def test_get_booking_by_id_admin_should_see_not_canceled_bookings(self):
        user_dto = UserDto('admin', True)
        manager = BookingManager(self.dummy_storage)
        res = manager.get_by_id(2, user_dto)
        self.assertEqual(res['code'], 'SUCCESS')

    def test_get_booking_by_id_non_admin_should_see_not_canceled_bookings(self):
        user_dto = UserDto('non_admin', False)
        manager = BookingManager(self.dummy_storage)
        res = manager.get_by_id(2, user_dto)
        self.assertEqual(res['code'], 'SUCCESS')

    def test_update_booking_requires_booking_id(self):
        checkin = datetime.utcnow()
        checkout = datetime.today()
        customer = CustomerDto("Customer", 18, "doc123", "a@a.com")
        booking_dto = DriverSchema(checkin=checkin, checkout=checkout, customer=customer)
        manager = BookingManager(self.dummy_storage)
        res = manager.update(booking_dto)
        self.assertEqual(res['code'], 'UPDATEBOOKINGREQUIRESBOOKINGID')

    def test_update_booking_should_fail_if_customer_is_not_older_than_18(self):
        checkin = datetime.utcnow()
        checkout = datetime.today()
        customer = CustomerDto("Customer", 17, "doc123", "a@a.com")
        booking_dto = DriverSchema(checkin=checkin, checkout=checkout, customer=customer)
        booking_dto.id = 1
        manager = BookingManager(self.dummy_storage)
        res = manager.update(booking_dto)
        self.assertEqual(res['code'], 'CUSTOMERSHOULDBEOLDERTHAN18')

    def test_update_booking_should_fail_if_customer_doc_is_invalid(self):
        checkin = datetime.utcnow()
        checkout = datetime.today()
        customer = CustomerDto("Customer", 18, "inv", "a@a.com")
        booking_dto = DriverSchema(checkin=checkin, checkout=checkout, customer=customer)
        booking_dto.id = 1
        manager = BookingManager(self.dummy_storage)
        res = manager.update(booking_dto)
        self.assertEqual(res['code'], 'INVALIDCUSTOMERDOCUMENT')    

    def test_update_booking_happy_path(self):
        checkin = datetime.utcnow()
        checkout = datetime.today()
        customer = CustomerDto("Customer", 18, "doc123", "a@a.com")
        booking_dto = DriverSchema(checkin=checkin, checkout=checkout, customer=customer)
        booking_dto.id = 1
        manager = BookingManager(self.dummy_storage)
        res = manager.update(booking_dto)
        self.assertEqual(res['code'], 'SUCCESS')    

if __name__ == '__main__':
    unittest.main()
