from entity.Vehicle import Vehicle

import mysql.connector

from myexceptions.CarNotFoundException import CarNotFoundException

con=mysql.connector.connect(
    host="localhost",user="root",password="root",port='3306',database="carrentalsystem")
cur=con.cursor()

class CarService:
    def add_car(self,vehicle:Vehicle):
        query = "insert into vehicle values({}, '{}', '{}', {}, {}, '{}', {}, {})".format(vehicle.vehicle_id,vehicle.make,
                                                                                          vehicle.model,vehicle.year,vehicle.daily_rate,
                                                                                          vehicle.status,vehicle.passenger_capacity,vehicle.engine_capacity)
        cur.execute(query)
        con.commit()
        print("data inserted successfully")

    def remove_car(self,id):
        query = "delete from vehicle where vehicleID={}".format(id)
        cur.execute(query)
        if cur.rowcount == 0:
            raise CarNotFoundException(id)
        con.commit()
        print("Car with vehicleID", id, "deleted successfully")




    def listAvailableCars(self):
        query = "select * from Vehicle where status='available'"
        cur.execute(query)
        records = cur.fetchall()
        if records:
            print(records)
            con.commit()
        else:
            print("No available cars")

    def update_car_availability(self):
        pass


    '''
    def findCarById(self, id):
        query = "SELECT * FROM Vehicle WHERE vehicleID = {0}".format(id)
        cur.execute(query)
        result = cur.fetchall()
        if result:
            for record in result:
                print(record)
            con.commit()
            print("car data with vehicleID", id, "fetched successfully")
        else:
            print("car data with vehicleID", id, "not found")
    '''

    def findCarById(self, id):
        query = "SELECT * FROM Vehicle WHERE vehicleID = {0}".format(id)
        cur.execute(query)
        result = cur.fetchall()
        if result:
            for record in result:
                print(record)
            con.commit()
            print("car data with vehicleID", id, "fetched successfully")
        else:
            raise CarNotFoundException(id)
            #print("car data with vehicleID", id, "not found")
    def RentedCars(self):
        query = "select * from Vehicle where status='notavailable'"
        cur.execute(query)
        records = cur.fetchall()
        if records:
            print(records)
            con.commit()
        else:
            print("No rented cars")



