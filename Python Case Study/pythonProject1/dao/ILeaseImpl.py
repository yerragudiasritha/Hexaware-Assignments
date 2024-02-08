from entity.Lease import Lease

import mysql.connector

from myexceptions.LeaseNotFoundException import LeaseNotFoundException

con = mysql.connector.connect(
    host="localhost",user="root",password="root",port='3306',database="carrentalsystem")
cur=con.cursor()
class LeaseService:
    def create_Lease(self,lease:Lease):
        query = ("insert into lease values({}, {}, {}, '{}','{}','{}')".format(lease.lease_id,lease.customer_id,
                                                                               lease.vehicle_id, lease.start_date,
                                                                               lease.end_date, lease.lease_type))

        cur.execute(query)
        con.commit()
        print("lease created successfully")


    def lease_info(self, lease_id):
        query = "SELECT * FROM Lease WHERE leaseID = {0}".format(lease_id)
        cur.execute(query)
        result = cur.fetchone()  # Since leaseID is unique, we fetch one record

        if result:
            lease_data = Lease(result[0],result[1],result[2],result[3],result[4],result[5])
            print("LeaseId :",result[0]," vehicleID:",result[1]," customerId:",result[2],
                  " StartDate:",result[3], " EndDate:",result[4]," leaseType:",result[5])
            con.commit()
            #print("Lease info with leaseID", lease_id, "fetched successfully")
            return lease_data

        else:
            raise LeaseNotFoundException(lease_id)

    def active_lease(self,date):
        query = "select * from Lease where endDate > '{}'".format(date)
        cur.execute(query)
        result = cur.fetchall()
        if result:
            for record in result:
                print(record)
            con.commit()
            print("Active leases fetched ...")
        else:
            print("No records found for active leases..")

    def lease_history(self,date):
        query = "select * from Lease where endDate < '{}'".format(date)
        cur.execute(query)
        result = cur.fetchall()
        if result:
            for record in result:
                print(record)
            con.commit()
            print("Lease history fetched ...")
        else:
            print("No records found for lease history..")

