class LeaseNotFoundException(Exception):#raised when lease id is not available in db.
    def __init__(self, lease_id):
        self.lease_id = lease_id
        #calling parent class of customexception .. parent class is Exception class
        super().__init__(f"Exception Raised: Lease with id {lease_id} not found")

