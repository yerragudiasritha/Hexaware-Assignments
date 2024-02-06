class Appointment:
    def __init__(self):
        self._appointmentId = None
        self._patientId = None
        self._doctorId = None
        self._appointmentDate = None
        self._description = None

    # Getter and setter for appointmentId
    def get_appointment_id(self):
        return self._appointmentId

    def set_appointment_id(self, appointment_id):
        self._appointmentId = appointment_id

    # Getter and setter for patientId
    def get_patient_id(self):
        return self._patientId

    def set_patient_id(self, patient_id):
        self._patientId = patient_id

    # Getter and setter for doctorId
    def get_doctor_id(self):
        return self._doctorId

    def set_doctor_id(self, doctor_id):
        self._doctorId = doctor_id

    # Getter and setter for appointmentDate
    def get_appointment_date(self):
        return self._appointmentDate

    def set_appointment_date(self, appointment_date):
        self._appointmentDate = appointment_date

    # Getter and setter for description
    def get_description(self):
        return self._description

    def set_description(self, description):
        self._description = description

