class CustomerNotFoundException(Exception):#raised when customer id is not available in db.
    def __init__(self, customer_id):
        self.customer_id = customer_id
        #calling parent class of customexception .. parent class is Exception class
        super().__init__(f"Exception Raised: Customer with id {customer_id} not found")