class Destination:
    def __init__(self, name, description, location, date, price):
        self.name = name
        self.description = description
        self.location = location
        self.date = date
        self.price = price

def load_destinations(file_path='destinations.txt'):
    destinations = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                name, description, location, date, price = line.strip().split(',')
                destinations.append(Destination(name, description, location, date, price))
    except FileNotFoundError:
        print("No destinations found.")
    return destinations

def search_destinations(destinations):
    search_term = input("Enter a destination or activity to search for: ").strip().lower()
    results = [dest for dest in destinations if search_term in dest.name.lower() or search_term in [activity.lower() for activity in dest.activities]]
    
    if results:
        print("Search Results:")
        for dest in results:
            print(f"Destination: {dest.name}")
            print(f"Description: {dest.description}")
            print(f"Location: {dest.location}")
            print(f"Date: {dest.date}")
            print(f"Price: {dest.price}")
            print("-" * 20)
    else:
        print("No destinations found matching your search.")
