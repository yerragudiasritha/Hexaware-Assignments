# entity/lease.py

class Lease:
    def __init__(self, lease_id=None, vehicle_id=None, customer_id=None, start_date=None, end_date=None, lease_type=None):
        self._lease_id = lease_id
        self._vehicle_id = vehicle_id
        self._customer_id = customer_id
        self._start_date = start_date
        self._end_date = end_date
        self._lease_type = lease_type

    # Getter and setter methods for lease_id
    @property
    def lease_id(self):
        return self._lease_id

    @lease_id.setter
    def lease_id(self, value):
        self._lease_id = value

    # Getter and setter methods for vehicle_id
    @property
    def vehicle_id(self):
        return self._vehicle_id

    @vehicle_id.setter
    def vehicle_id(self, value):
        self._vehicle_id = value

    # Getter and setter methods for customer_id
    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value

    # Getter and setter methods for start_date
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value

    # Getter and setter methods for end_date
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value

    # Getter and setter methods for lease_type
    @property
    def lease_type(self):
        return self._lease_type

    @lease_type.setter
    def lease_type(self, value):
        self._lease_type = value
