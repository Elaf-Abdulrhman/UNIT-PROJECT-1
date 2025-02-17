from home import User, register, login, load_users

def main():
    print("Welcome to the (....) system")
    users = load_users()
    
    while True:
        choice = input("Do you want to register or login? (register/login): ").strip().lower()
        if choice == 'register':
            users = register(users)
        elif choice == 'login':
            users = login(users)
        else:
            print("Invalid choice. Please choose 'register' or 'login'.")
        continue_choice = input("Do you want to continue? (yes/no): ").strip().lower()
        if continue_choice != 'yes':
            break

if __name__ == "__main__":
    main()
