from tourist.destinations import Destination, load_destinations

def add_destination(destinations, file_path='destinations.txt'):
    name = input("Enter destination name: ")
    
    if name.lower() in destinations:
        print("Destination already exists! Please choose a different name.")
        return destinations
    
    description = input("Enter destination description: ")
    location = input("Enter destination location: ")
    date = input("Enter destination date: ")
    price = input("Enter destination price: ")
    
    destinations[name] = Destination(name, description, location, date, price)

    try:
        with open(file_path, 'a') as file:
            file.write(f"{name},{destinations[name].description},{destinations[name].location},{destinations[name].date},{destinations[name].price}\n")
        print("Destination added successfully!")
    except IOError as e:
        print(f"Error saving destination data: {e}")
    
    return destinations

def delete_destination(file_path='destinations.txt'):
    name = input("Enter destination name to delete: ")
    
    destinations = load_destinations(file_path)
    
    if name.lower() in destinations:
        del destinations[name]
        
        try:
            with open(file_path, 'w') as file:
                for dest in destinations.values():
                    file.write(f"{dest.name},{dest.description},{dest.location},{dest.date},{dest.price}\n")
            print("Destination deleted successfully!")
        except IOError as e:
            print(f"Error saving destination data: {e}")
    else:
        print("Destination not found.")

def list_destinations(destinations):
    if not destinations:
        print("No destinations available.")
        return
    
    for dest in destinations.values():
        print(f"Name: {dest.name}")
        print(f"Description: {dest.description}")
        print(f"Location: {dest.location}")
        print(f"Date: {dest.date}")
        print(f"Price: {dest.price}")
        print("-" * 20)

def handle_support_user():
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