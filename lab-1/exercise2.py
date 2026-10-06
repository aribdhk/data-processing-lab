CHILD_DISCOUNT = 0.50
STUDENT_DISCOUNT = 0.25
SENIOR_DISCOUNT = 0.40

print(" Train Ticket Booking (from Dhaka) ")
print("Destinations and adult fares:")
print("1. Chattogram - 650 BDT")
print("2. Sylhet     - 550 BDT")
print("3. Rajshahi   - 500 BDT")
print("4. Khulna     - 600 BDT")
print()

name = input("Enter passenger name: ")
phone = input("Enter phone number: ")

destination_choice = int(input("Choose destination (1-4): "))
while destination_choice < 1 or destination_choice > 4:
    print("Invalid choice. Enter a number from 1 to 4.")
    destination_choice = int(input("Choose destination (1-4): "))

if destination_choice == 1:
    destination = "Chattogram"
    fare = 650
elif destination_choice == 2:
    destination = "Sylhet"
    fare = 550
elif destination_choice == 3:
    destination = "Rajshahi"
    fare = 500
else:
    destination = "Khulna"
    fare = 600

tickets = int(input("Enter number of tickets: "))
while tickets < 1:
    print("You must buy at least 1 ticket.")
    tickets = int(input("Enter number of tickets: "))

print()
print("Passenger types: 1. Adult  2. Child  3. Student  4. Senior")
type_choice = int(input("Choose passenger type (1-4): "))
while type_choice < 1 or type_choice > 4:
    print("Invalid choice. Enter a number from 1 to 4.")
    type_choice = int(input("Choose passenger type (1-4): "))

if type_choice == 1:
    passenger_type = "Adult"
    discount = 0
elif type_choice == 2:
    passenger_type = "Child"
    discount = CHILD_DISCOUNT
elif type_choice == 3:
    passenger_type = "Student"
    discount = STUDENT_DISCOUNT
else:
    passenger_type = "Senior"
    discount = SENIOR_DISCOUNT

price_per_ticket = fare - fare * discount
total_fare = price_per_ticket * tickets

print()
print(" TRAIN TICKET ")
print("Passenger      :", name)
print("Phone          :", phone)
print("From           : Dhaka")
print("To             :", destination)
print("Passenger type :", passenger_type)
print("Tickets        :", tickets)
print("Fare per ticket:", round(price_per_ticket, 2), "BDT")
print("Total fare     :", round(total_fare, 2), "BDT")
print("------------------------------------------")
