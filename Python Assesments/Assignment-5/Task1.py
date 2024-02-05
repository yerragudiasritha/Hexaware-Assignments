
class Task1:
    def __init__(self):
        print("First 3 tasks")

    def checkTicketAvailability(self):
        print("Enter the available tickets and Number of  tickets Required")
        availableTickets = int(input())
        noOfTickets = int(input())
        if availableTickets > noOfTickets:
            print("The required number of tickets are available")
        else:
            print("The tickets are not available ")

    def calculateTotalCost(self):
        ticketType = input("Please enter ticket type : ")
        noOfTickets = int(input("Please enter no of tickets : "))
        base = 0
        if ticketType == "Silver":
            base = 50
        elif ticketType == "Gold":
            base = 100
        elif ticketType == "Diamond":
            base = 150
        print(f"Total cost of tickets will be {base * noOfTickets}")

    def looping(self):
        ticketType = input("Please enter ticket type : ")
        while ticketType != "Exit":
            noOfTickets = int(input("Please enter no of tickets : "))
            base = 0
            if ticketType == "Silver":
                base = 50
            elif ticketType == "Gold":
                base = 100
            elif ticketType == "Diamond":
                base = 150
            print(f"Total cost of tickets is {base * noOfTickets}")
            ticketType = input("Please enter ticket type : ")
