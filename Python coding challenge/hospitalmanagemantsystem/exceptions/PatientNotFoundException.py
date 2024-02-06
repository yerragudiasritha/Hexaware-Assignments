class PatientNumberNotFoundException(Exception):
    def __init__(self, patient_id):
        self.patient_id = patient_id
        super().__init__(f" Patient with id {patient_id} not found")


