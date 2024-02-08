import unittest
import datetime

from entity.Lease import Lease
from entity.Vehicle import Vehicle
from dao.ILeaseImpl import LeaseService
from myexceptions.LeaseNotFoundException import LeaseNotFoundException


class TestCar(unittest.TestCase):
    def test_car_creation(self):
        car_data = Vehicle(10,'swift','camry',2021,60.00,'available',7,1.2)
        #assertequals(expected,actual)
        self.assertEqual(car_data.vehicle_id,10)
        self.assertEqual(car_data.make,'swift')
        self.assertEqual(car_data.model,'camry')
        self.assertEqual(car_data.year,2021)
        self.assertEqual(car_data.daily_rate,60.00)
        self.assertEqual(car_data.status,'available')
        self.assertEqual(car_data.passenger_capacity,7)
        self.assertEqual(car_data.engine_capacity,1.2)

    def test_lease_creation(self):
        lease_data = Lease(1,1,1,'2024-2-5','2024-2-10','monthly')
        self.assertEqual(lease_data.lease_id,1)
        self.assertEqual(lease_data.vehicle_id, 1)
        self.assertEqual(lease_data.customer_id, 1)
        self.assertEqual(lease_data.start_date, '2024-2-5')
        self.assertEqual(lease_data.end_date, '2024-2-10')
        self.assertEqual(lease_data.lease_type, 'monthly')

    import datetime

    def test_retrieve_lease(self):
        data = LeaseService()
        id_to_retrieve = 1
        expected_data = {'lease_id': 1, 'vehicle_id': 1, 'customer_id': 1, 'start_date': datetime.date(2024, 2, 1),
                         'end_date': datetime.date(2024, 2, 5), 'lease_type': 'DailyLease'}
        actual_data = data.lease_info(id_to_retrieve)

        # Convert actual_data object to dictionary because expected data is in dictionary format
        actual_data_dict = {
            'lease_id': actual_data.lease_id,
            'vehicle_id': actual_data.vehicle_id,
            'customer_id': actual_data.customer_id,
            'start_date': actual_data.start_date,
            'end_date': actual_data.end_date,
            'lease_type': actual_data.lease_type
        }

        # Compare dictionaries
        self.assertEqual(actual_data_dict['lease_id'], expected_data['lease_id'])
        self.assertEqual(actual_data_dict['vehicle_id'], expected_data['vehicle_id'])
        self.assertEqual(actual_data_dict['customer_id'], expected_data['customer_id'])
        self.assertEqual(actual_data_dict['start_date'], expected_data['start_date'])
        self.assertEqual(actual_data_dict['end_date'], expected_data['end_date'])
        self.assertEqual(actual_data_dict['lease_type'], expected_data['lease_type'])

    # testing exception is thrown when customerid/vehid/leaseid is not in DB.

    def test_leaseNotFoundException(self):
        lease_object = LeaseService()
        lease_id = 100
        expected =f"Exception Raised: Lease with id {lease_id} not found"
        with self.assertRaises(LeaseNotFoundException) as context:
            lease_object.lease_info(lease_id)

        self.assertEqual(str(context.exception), expected)






