class CarNotFoundException(Exception):
    #raised when car id is not available in db.
    def __init__(self, car_id):
        self.car_id = car_id
        #calling parent class of customexception .. parent class is Exception class
        super().__init__(f"Exception Raised: car with id {car_id} not found")




