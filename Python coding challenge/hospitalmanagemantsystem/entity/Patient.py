class Patient:
    def __init__(self, patientId, firstName, lastName, dateOfBirth, gender, contactNumber, address):
        self._patientId = patientId
        self._firstName = firstName
        self._lastName = lastName
        self._dateOfBirth = dateOfBirth
        self._gender = gender
        self._contactNumber = contactNumber
        self._address = address

    def display_patient_info(self):
        print(f"Patient ID: {self._patientId}")
        print(f"First Name: {self._firstName}")
        print(f"Last Name: {self._lastName}")
        print(f"Date of Birth: {self._dateOfBirth}")
        print(f"Gender: {self._gender}")
        print(f"Contact Number: {self._contactNumber}")
        print(f"Address: {self._address}")

