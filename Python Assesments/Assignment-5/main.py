import mysql.connector
con = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="root",
    database="ticketbookingsystem"
)
venue = "VSK Hall"
cur = con.cursor()
cur.execute("select venue_id from venue where venue_name= %s", (venue,))
venue_id = cur.fetchone()
print(venue_id[0])

"""
    event = {
        "event_name" : input("Enter the event name of the event: "),
        "event_date" : input("Enter the date : "),
        "event_time" : input("Enter the Event timing : "),
        "venue_name" : input("Enter venue name : "),
        "total_seats" : int(input("Enter total seats in the hall")),
        "available_seats" : int(input("Enter available seats in the hall: ")),
        "ticket_price" : float(input("Enter the ticket price : ")),
        "event_type" : input("Enter type of the event : ")
    }
    booking = Booking(event)
    print(booking.getBookedNoOfTickets())

"""
