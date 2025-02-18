import calendar
from colorama import init, Fore, Style
from datetime import datetime

# Initialize colorama
init(autoreset=True)

class Destination:
    def __init__(self, name, description, location, date, price):
        self.name = name
        self.description = description
        self.location = location
        self.date = date  # Expect date in 'YYYY-MM-DD' format
        self.price = price

def load_destinations(file_path='destinations.txt'):
    destinations = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                values = line.strip().split(',')
                if len(values) == 5:
                    name, description, location, date, price = values
                    # Ensure the date is in a consistent format
                    try:
                        datetime.strptime(date, "%Y-%m-%d")  # Validate date format
                        destinations[name] = Destination(name, description, location, date, price)
                    except ValueError:
                        print(f"Invalid date format for destination: {name}")
                else:
                    print(f"Skipping invalid line (expected 5 values, got {len(values)}): {line.strip()}")
    except FileNotFoundError:
        print("No destinations found.")
    return destinations

def search_destinations(destinations):
    search_term = input("Enter a destination or activity to search for: ").strip().lower()
    results = [dest for dest in destinations.values() if search_term in dest.name.lower()]

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

def book_destination(destinations, booked_dates):
    destination_name = input("Enter the name of the destination you want to book: ").strip()
    if destination_name in destinations:
        date = destinations[destination_name].date  # Date from the destination object
        booked_dates.add(date)  # Add the booked date to the set
        print(f"You have successfully booked {destination_name} on {date}.")
    else:
        print("Destination not found.")

def display_calendar(year, month, booked_dates):
    # Get the month's calendar
    cal = calendar.monthcalendar(year, month)

    # Print the month and year
    print(f"Booked activites for {calendar.month_name[month]} {year}")
    print("Mo Tu We Th Fr Sa Su")  # Print days of the week header

    # Loop through each week in the month
    for week in cal:
        for day in week:
            if day == 0:
                print("   ", end="  ")  # Empty space for days outside the month
            else:
                # Check if the date is booked
                current_date = f"{year}-{month:02d}-{day:02d}"
                if current_date in booked_dates:
                    print(Fore.RED + f"{day:2}", end="  ")  # Use colorama for red color
                else:
                    print(f"{day:2}", end="  ")
        print()  # New line after each week