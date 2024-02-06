class Doctor:
    def __init__(self, doctorId, firstName, lastName, specialization, contactNumber):
        self._doctorId = doctorId
        self._firstName = firstName
        self._lastName = lastName
        self._specialization = specialization
        self._contactNumber = contactNumber

    def display_doctor_info(self):
        print(f"Doctor ID: {self._doctorId}")
        print(f"First Name: {self._firstName}")
        print(f"Last Name: {self._lastName}")
        print(f"Specialization: {self._specialization}")
        print(f"Contact Number: {self._contactNumber}")

