# entity/vehicle.py

class Vehicle:
    def __init__(self, vehicle_id=None, make=None, model=None, year=None, daily_rate=None,
                 status=None, passenger_capacity=None, engine_capacity=None):
        self._vehicle_id = vehicle_id
        self._make = make
        self._model = model
        self._year = year
        self._daily_rate = daily_rate
        self._status = status
        self._passenger_capacity = passenger_capacity
        self._engine_capacity = engine_capacity

    # Getter and setter methods for vehicle_id
    @property
    def vehicle_id(self):
        return self._vehicle_id

    @vehicle_id.setter
    def vehicle_id(self, value):
        self._vehicle_id = value

    # Getter and setter methods for make
    @property
    def make(self):
        return self._make

    @make.setter
    def make(self, value):
        self._make = value

    # Getter and setter methods for model
    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value

    # Getter and setter methods for year
    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value

    # Getter and setter methods for daily_rate
    @property
    def daily_rate(self):
        return self._daily_rate

    @daily_rate.setter
    def daily_rate(self, value):
        self._daily_rate = value

    # Getter and setter methods for status
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    # Getter and setter methods for passenger_capacity
    @property
    def passenger_capacity(self):
        return self._passenger_capacity

    @passenger_capacity.setter
    def passenger_capacity(self, value):
        self._passenger_capacity = value

    # Getter and setter methods for engine_capacity
    @property
    def engine_capacity(self):
        return self._engine_capacity

    @engine_capacity.setter
    def engine_capacity(self, value):
        self._engine_capacity = value

