import calendar
import matplotlib.pyplot as plt

class Destination:
    def __init__(self, name, description, location, date, price):
        self.name = name
        self.description = description
        self.location = location
        self.date = date
        self.price = price

def show_calendar(booked_dates=None):
    year = int(input("Enter the year: "))
    month = int(input("Enter the month: "))
    
    cal = calendar.monthcalendar(year, month)
    
    fig, ax = plt.subplots()
    ax.set_axis_off()
    
    table_data = []
    for week in cal:
        week_data = []
        for day in week:
            if day == 0:
                week_data.append("")
            else:
                date_str = f"{year}-{month:02d}-{day:02d}"
                if booked_dates and date_str in booked_dates:
                    week_data.append(f"{day} (X)")
                else:
                    week_data.append(str(day))
        table_data.append(week_data)
    
    table = ax.table(cellText=table_data, cellLoc='center', loc='center')
    table.scale(1, 2)
    
    plt.title(calendar.month_name[month] + " " + str(year))
    plt.show()

def load_destinations(file_path='destinations.txt'):
    destinations = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                values = line.strip().split(',')
                if len(values) == 5:
                    name, description, location, date, price = values
                    destinations[name] = Destination(name, description, location, date, price)
                else:
                    print(f"Skipping invalid line: {line.strip()}")
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
        date = destinations[destination_name].date
        booked_dates.add(date)
        print(f"You have successfully booked {destination_name} on {date}.")
    else:
        print("Destination not found.")

