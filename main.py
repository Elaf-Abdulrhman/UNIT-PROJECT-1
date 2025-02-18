from home import User, register, login, load_users
from support.destination import load_destinations
from tourist.destinations import search_destinations
from support.handle import handle_support_user
from tourist.handle import handle_tourist_user

def main():
    print("Welcome to the (....) system")
    users = load_users()  # Load existing users from file
    
    try:
        while True:
            choice = input("Do you want to register or login? (register/login): write 'e' to exit ").strip().lower()
            if choice == 'register':
                users = register(users)  # Register new user
            elif choice == 'login':
                users, logged_in_user = login(users)  # Login existing user
                if logged_in_user:
                    if logged_in_user.user_type == 'support':
                        handle_support_user()  # Support user functionality
                    elif logged_in_user.user_type == 'tourist':
                        handle_tourist_user()  # Tourist user functionality
                else:
                    print("Login failed. Please try again.")
            elif choice == 'e':
                print("Exiting the system...")
                break
            else:
                print("Invalid choice. Please choose 'register' or 'login'.")
                continue  # Skip the rest of the loop and prompt again
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")

if __name__ == "__main__":
    main()
