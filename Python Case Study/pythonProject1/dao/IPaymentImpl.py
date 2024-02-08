
import mysql.connector

from entity.Lease import Lease

con=mysql.connector.connect(
    host="localhost",user="root",password="root",port='3306',database="carrentalsystem")
cur = con.cursor()


class PaymentService:

    def record_Payment(self,lease_info: Lease,payment_id):
        cur.execute("select datediff('{0}','{1}') as days from Lease where leaseId={2}".format(lease_info.end_date,
                                                                                               lease_info.start_date,
                                                                                               lease_info.lease_id))
        no_of_days = cur.fetchone()[0]

        cur.execute("select dailyRate from Vehicle where vehicleID={}".format(lease_info.vehicle_id))
        price_per_day = cur.fetchone()[0]
        total_amt = no_of_days * price_per_day
        query = "insert into Payment values({},{},'{}',{})".format(payment_id,lease_info.lease_id,lease_info.end_date,total_amt)
        cur.execute(query)
        con.commit()
        print("payment generated successfully and the amt for ",no_of_days,'days is :',total_amt)


    #Payment History of a Customer

    def payment_history_of_customer(self,cust_id):
        query ="select leaseId from Lease where customerid={}".format(cust_id)
        cur.execute(query)
        leases=cur.fetchall()
        if leases:
            for lease in leases:
                lease_id = lease[0]
                que = "select * from Payment where leaseId={}".format(lease_id)
                cur.execute(que)
                result = cur.fetchone()
                print(result)
            con.commit()
        else:
            print("NO RECORDS FOUND")


    #Calculating total Revenue
    def total_revenue(self):
        query = "select SUM(amount) AS money FROM Payment"
        cur.execute(query)
        result=cur.fetchone()
        if result:
            amt= result[0]
        else:
            amt=0
        con.commit()
        print("total revenue generated and the Amount is :",amt)












