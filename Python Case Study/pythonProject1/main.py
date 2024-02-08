from datetime import datetime
from dao.ICarLeaseImpl import CarService
from dao.ICustomerImpl import CustomerServices
from dao.ILeaseImpl import LeaseService
from dao.IPaymentImpl import PaymentService
from entity.Customer import Customer
from entity.Lease import Lease
from entity.Vehicle import Vehicle
from myexceptions.CarNotFoundException import CarNotFoundException
from myexceptions.CustomerNotFoundException import CustomerNotFoundException
from myexceptions.LeaseNotFoundException import LeaseNotFoundException

car_service= CarService()
customer_service=CustomerServices()
lease_service=LeaseService()
payment_service = PaymentService()

while True:
    print("***** Welcome To CarRentalSystem *****")
    print("** Select Options :**")
    print("1.Add new Car:")
    print("2.Remove Car:")
    print("3.Display Available Cars:")
    print("4.Display Car by id:")
    print("5.Display Rented Cars:")
    print("6.Update customer Information:")
    print("7.Add new Customer:")
    print("8.Remove Customer:")
    print("9.List All Customers:")
    print("10.Find Customer by id:")
    print("11.Create Lease:")
    print("12.Lease info by id:")
    print("13.list Active Lease:")
    print("14.list Lease History:")
    print("15.Record Payments..")
    print("16.payment History of a Customer..")
    print("17.Total Revenue from Payments:")
    print("0.For Exit")
    print("******************")
    option=int(input("Enter number to perform operations:"))
    while option!=0:
        if option == 1:
            vehId = int(input("enter veh id"))
            name = input("enter make of car")
            model = input("enter model of car")
            yer = int(input("enter model year "))
            rate_per_day = int(input("enter rate "))
            status = input("enter status")
            passengerCap = int(input("enter capacity of passengers"))
            engineCap = float(input("enter capacity of engine"))
            # objectnameof class car=Car()
            # carObject=Vehicle();
            vehicle = Vehicle(vehId, name, model, yer, rate_per_day, status, passengerCap, engineCap)
            car_service.add_car(vehicle)
            break

        if option == 2:
            try:
                vehId = int(input("enter veh id to delete"))
                car_service.remove_car(vehId)
            except CarNotFoundException as e:
                print(e)
            break

        if option == 3:
            car_service.listAvailableCars()
            break

        if option == 4:
            try:
                car_id = int(input("enter veh id to display"))
                car_service.findCarById(car_id)
            except CarNotFoundException as e:
                print(e)
            break

        if option == 5:
            car_service.RentedCars()
            break

        if option == 6:
            custId = int(input("enter cust id"))
            firstname = input("enter first name")
            customer_service.updatecustomer(custId,firstname)
            break

        if option == 7:
            custId = int(input("enter cust id"))
            firstname = input("enter firstname of customer")
            lastname = input("enter lastname of customer")
            email = input("enter email")
            phonenum = int(input("enter phone number "))
            customerData = Customer(custId, firstname, lastname, email, phonenum)
            customer_service.add_customer(customerData)
            break

        if option == 8:
            customerId = int(input("enter customer id to delete"))
            customer_service.remove_customer(customerId)
            break
        if option == 9:
            customer_service.list_all_customers()
            break

        if option == 10:
            try:
                customerId = int(input("enter customer id"))
                customer_service.findCustomerById(customerId)
            except CustomerNotFoundException as e:
                print(e)
            break

        if option == 11:
            leaseId = int(input("enter lease id"))
            custId = int(input("enter customer id"))
            vehId = int(input("enter veh id"))
            start = input("enter startdate (YYYY-MM-DD):")
            end = input("enter enddate (YYYY-MM-DD):")
            lease_type = input("enter leasetype:")
            leaseData = Lease(leaseId, custId, vehId, start, end,lease_type)
            lease_service.create_Lease(leaseData)
            break

        if option == 12:
            try:
                leaseId = int(input("enter lease id to display"))
                lease_service.lease_info(leaseId)
                #print(output)

            except LeaseNotFoundException as e:
                print(e)
            break

        if option == 13:
            search_date = input("enter today's date to search for active leases :")
            lease_service.active_lease(search_date)
            break

        if option == 14:
            date = input("enter today's date to search for lease history:")
            lease_service.lease_history(date)
            break

        #record payment
        if option == 15:
            payment_id = int(input("enter payment id: "))
            lease_id = int(input("enter lease id to fetch details:"))
            data = lease_service.lease_info(lease_id)
            payment_service.record_Payment(data,payment_id)

            break

        if option == 16:
            customer_id=int(input("Enter Customer ID To Find His/Her Payment History"))
            payment_service.payment_history_of_customer(customer_id)
            break

        if option == 17:
            payment_service.total_revenue()
            break










