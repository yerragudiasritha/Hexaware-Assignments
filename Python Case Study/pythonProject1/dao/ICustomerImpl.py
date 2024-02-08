from entity.Customer import Customer
# entity.filename import class name
import mysql.connector

from myexceptions.CustomerNotFoundException import CustomerNotFoundException

con=mysql.connector.connect(
    host="localhost",user="root",password="root",port='3306',database="carrentalsystem")
cur=con.cursor()
class CustomerServices:
    def add_customer(self, customer: Customer):
        query = "insert into customer values({}, '{}', '{}', '{}', {})".format(customer.customer_id,
                                                                                          customer.first_name,
                                                                                          customer.last_name,customer.email,
                                                                                          customer.phone_number)
        cur.execute(query)
        con.commit()
        print("data inserted successfullyy")

    def remove_customer(self,id):
        query = "delete from customer where customerID={}".format(id)
        cur.execute(query)
        con.commit()
        print("customer with customerID",id, "deleted successfully")

    #def update_customer(self,newdata: Customer):


    def list_all_customers(self):
        query = "select * from Customer"
        cur.execute(query)
        records = cur.fetchall()
        if records:
            print(records)
            con.commit()
        else:
            print("No customers")

    def findCustomerById(self, id):
        query = "SELECT * FROM Customer WHERE customerID = {0}".format(id)
        cur.execute(query)
        result = cur.fetchall()
        if result:
            for record in result:
                print(record)
            con.commit()
            print("customer data with customerID", id, "fetched successfully")
        else:
            raise CustomerNotFoundException(id)

    def updatecustomer(self, id, new_firstname):
        query = "UPDATE Customer SET firstName = '{}' WHERE customerId = {}".format(new_firstname, id)
        cur.execute(query)
        con.commit()
        print("customer with customerID", id, "Updated successfully")











