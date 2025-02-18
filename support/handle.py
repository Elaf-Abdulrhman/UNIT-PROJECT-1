from support.destination import load_destinations, add_destination, delete_destination, list_destinations
from tourist.destinations import search_destinations 
def handle_support_user():
    # Functionality for support users to manage destinations
    while True:
        print("\nSupport User Options:")
        print("1. Add destination")
        print("2. Delete destination")
        print("3. List destinations")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            # Add destination
            destinations = load_destinations()
            add_destination(destinations)
        elif choice == '2':
            # Delete destination
            delete_destination()
        elif choice == '3':
            # List destinations
            destinations = load_destinations()
            list_destinations(destinations)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please choose a valid option.")