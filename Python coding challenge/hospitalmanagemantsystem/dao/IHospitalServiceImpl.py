from entity.Appointment import Appointment
import mysql.connector

from exceptions.PatientNotFoundException import PatientNumberNotFoundException

con=mysql.connector.connect(
    host="localhost",user="root",password="root",port='3306',database="hospitalmanagementsystem")
cur=con.cursor()
class HospitalService:
    def get_appointmentById(self, id):
        query = "SELECT * FROM Appointment WHERE appointmentID = {0}".format(id)
        cur.execute(query)
        result = cur.fetchall()
        if result:
            for record in result:
                print(record)
            con.commit()
            print("appointment data with appointmentID", id, "fetched successfully")
        else:
            print("appointment data with appointmentID", id, "not found")

    def get_appointmentBypatientId(self,id):
        query = "SELECT * FROM Appointment WHERE patientID = {0}".format(id)
        cur.execute(query)
        result = cur.fetchall()
        if result:
            for record in result:
                print(record)
            con.commit()
            print("appointment data with patientID", id, "fetched successfully")
        else:
            raise PatientNumberNotFoundException(id)

    def cancelAppointment(self,appointment_id):
        query = "delete from Appointment where appointmentID = {0}".format(appointment_id)
        cur.execute(query)
        con.commit()
        print("Appointment with ID", appointment_id, "deleted successfully")


    def get_all_appointmentByDoctorId(self,id):
        query = "SELECT * FROM Appointment WHERE doctorId = {0}".format(id)
        cur.execute(query)
        result = cur.fetchall()
        if result:
            for record in result:
                print(record)
            con.commit()
            print("All appointments of Doctor with Doctor id:",id,"Fetched Successfully")
        else:
            print("appointments of Doctor with Doctor id:", id, "not found")








    '''
    
    if option == 5:
            appointmentid = int(input("enter appointment id"))
            patientid = int(input("enter patient id"))
            doctorid = int(input("enter doctor id"))
            appointmentdate = (input("enter date "))
            description = (input("enter description "))
            appointment_data = Appointment(appointmentid, patientid, doctorid, appointmentdate,description)
            hospital_service.schedule_appointment(appointment_data)
            break
    def schedule_appointment(self,xyz: Appointment):
        query = "insert into Appointment values({},{},{},'{}','{}')".format(xyz.)

        cur.execute(query)
        con.commit()
        print("appointment scheduled successfully")
    '''



