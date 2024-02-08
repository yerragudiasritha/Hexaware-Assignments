# entity/payment.py

class Payment:
    def __init__(self, payment_id=None, lease_id=None, payment_date=None, amount=None):
        self._payment_id = payment_id
        self._lease_id = lease_id
        self._payment_date = payment_date
        self._amount = amount

    # Getter and setter methods for payment_id
    @property
    def payment_id(self):
        return self._payment_id

    @payment_id.setter
    def payment_id(self, value):
        self._payment_id = value

    # Getter and setter methods for lease_id
    @property
    def lease_id(self):
        return self._lease_id

    @lease_id.setter
    def lease_id(self, value):
        self._lease_id = value

    # Getter and setter methods for payment_date
    @property
    def payment_date(self):
        return self._payment_date

    @payment_date.setter
    def payment_date(self, value):
        self._payment_date = value

    # Getter and setter methods for amount
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
