from PROJECT.tourist.destinations import Destination, load_destinations

def add_destination(destinations, file_path='destinations.txt'):
    name = input("Enter destination name: ")
    
    # Check if the destination already exists
    if name.lower() in destinations:
        print("Destination already exists! Please choose a different name.")
        return destinations
    
    description = input("Enter destination description: ")
    location = input("Enter destination location: ")
    date = input("Enter destination date: ")
    price = input("Enter destination price: ")
    
    # Create a new destination and store it in the destinations dictionary
    destinations[name] = Destination(name, description, location, date, price)

    # Save the destination to a file
    try:
        with open(file_path, 'a') as file:
            file.write(f"{name},{destinations[name].description},{destinations[name].location},{destinations[name].date},{destinations[name].price}\n")
        print("Destination added successfully!")
    except IOError as e:
        print(f"Error saving destination data: {e}")
    
    return destinations

def delete_destination(file_path='destinations.txt'):
    name = input("Enter destination name to delete: ")
    
    # Load destinations from file
    destinations = load_destinations(file_path)
    
    # Check if the destination exists
    if name.lower() in destinations:
        del destinations[name]
        
        # Save the updated destinations to the file
        try:
            with open(file_path, 'w') as file:
                for dest in destinations.values():
                    file.write(f"{dest.name},{dest.description},{dest.location},{dest.date},{dest.price}\n")
            print("Destination deleted successfully!")
        except IOError as e:
            print(f"Error saving destination data: {e}")
    else:
        print("Destination not found.")