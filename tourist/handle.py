from tourist.destinations import load_destinations, search_destinations, book_destination, show_calendar

def handle_tourist_user():
    destinations = load_destinations()  # Load destinations here
    booked_dates = set()  # Initialize booked_dates as a set
    while True:
        print("\nTourist User Options:")
        print("1. Search destinations")
        print("2. Book destination")
        print("3. Show calendar with booked dates")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            # Search destinations
            search_destinations(destinations)
        elif choice == '2':
            # Book destination
            book_destination(destinations, booked_dates)
        elif choice == '3':
            # Show calendar with booked dates
            show_calendar(booked_dates)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please choose a valid option.")