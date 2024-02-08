# entity/customer.py

class Customer:
    def __init__(self, customer_id=None, first_name=None, last_name=None, email=None, phone_number=None):
        self._customer_id = customer_id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._phone_number = phone_number

    # Getter and setter methods for customer_id
    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value

    # Getter and setter methods for first_name
    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    # Getter and setter methods for last_name
    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    # Getter and setter methods for email
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    # Getter and setter methods for phone_number
    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value
