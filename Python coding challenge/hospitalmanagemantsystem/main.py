from dao.IHospitalServiceImpl import HospitalService
from exceptions.PatientNotFoundException import PatientNumberNotFoundException

hospital_service = HospitalService()
while True:
    print("select options:")
    print("1.get appoint by appointment id")
    print("2.get appoint by Patient id")
    print("3. Cancel/Delete Appoint by Appointment_id")
    print("4.get all appoints of Doctor by doctorId")
    print("******************")
    option = int(input("Enter number to perform operations"))
    while option != 0:
        if option == 1:
            appointment_id = int(input("enter appointment id"))
            hospital_service.get_appointmentById(appointment_id)
            break

        if option == 2:
            try:
                patient_id = int(input("enter patient id"))
                hospital_service.get_appointmentBypatientId(patient_id)
            except PatientNumberNotFoundException as e:
                print(e)
            break

        if option == 3:
            appointment_id = int(input("enter Appointment id to cancel"))
            hospital_service.cancelAppointment(appointment_id)
            break

        if option == 4:
            doc_id = int(input("enter Doctor id to fetch all appointments"))
            hospital_service.get_all_appointmentByDoctorId(doc_id)
            break
