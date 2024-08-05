flights = {
    "Pk1010": {"origin": "Dubai", "destination": "London", "seats": 200},
    "Pk1211": {"origin": "NewYork", "destination": "Karachi", "seats": 500}
}

reservations = {
    "Pk1010": [],
    "Pk1211": [],
}

def view_flight():
    print("Available flights:")
    for flightid, details in flights.items():
        print(f"Flight {flightid}, Origin: {details['origin']}, Destination: {details['destination']}, Seats Available: {details['seats']}")

def book_flight(flightid, passenger_name):
    if flightid not in flights:
        print("Flight not found")
        return
    if flights[flightid]['seats'] <= 0:
        print("Seats not available")
        return
    flights[flightid]['seats'] -= 1
    reservations[flightid].append(passenger_name)
    print(f"Booking confirmed for {passenger_name} on Flight ID {flightid}")

def reservation_list(flightid):
    if flightid not in reservations:
        print("Invalid Flight ID")
        return
    if not reservations[flightid]:
        print("No reservations for this flight")
        return
    print(f"Reservations for flight {flightid}:")
    for passenger in reservations[flightid]:
        print(f"- {passenger}")

def main():
    while True:
        print("\nFlight Reservation")
        print("1. List Reservations")
        print("2. View Flights")
        print("3. Book Flight")
        print("4. Exit")
        user_choice = input("Enter your choice: ")

        if user_choice == '1':
            flightid = input("Enter Flight ID: ")
            reservation_list(flightid)
        elif user_choice == '2':
            view_flight()
        elif user_choice == '3':
            flightid = input("Enter Flight ID: ")
            passenger_name = input("Enter Passenger Name: ")
            book_flight(flightid, passenger_name)
        elif user_choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
