# Description: This file contains the functions for the login system (login, register)
import hashlib  # for hashing passwords

class User:
    def __init__(self, username, password, user_type, is_hashed=False):
        self.username = username
        self.password = self.hash_password(password) if not is_hashed else password
        self.user_type = user_type
        
    def __str__(self):
        return f"User(username={self.username}, user_type={self.user_type})"

    def hash_password(self, password):
        # Hash the password using SHA-256
        return hashlib.sha256(password.encode()).hexdigest()

def register(users):
    username = input("Enter username: ")
    
    # Check if the username already exists
    if username in users:
        print("Username already exists! Please choose a different username.")
        return register(users)
    
    password = input("Enter password: ")  # maybe add a password strength checker later ***********
    user_type = input("Enter user type (tourist/support): ").strip().lower()
    
    # Create a new user and store it in the users dictionary
    users[username] = User(username, password, user_type)

    # Save the user to a file (store the hashed password and user type)
    try:
        with open('logins.txt', 'a') as file:
            file.write(f"{username},{users[username].password},{user_type}\n")  # Save hashed password and user type
        print("You have been registered successfully!")
    except IOError as e:  # Handle file I/O errors
        print(f"Error saving user data: {e}")

    return users

def login(users):
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if username in users and users[username].password == hashlib.sha256(password.encode()).hexdigest():
        print(f"Login successful! You are logged in as a {users[username].user_type}.")
        return users, users[username]
    else:
        print("Incorrect username or password.")
        return users, None

def load_users():
    users = {}
    try:
        with open('logins.txt', 'r') as file:
            for line in file:
                username, password, user_type = line.strip().split(',')
                users[username] = User(username, password, user_type, is_hashed=True)
    except FileNotFoundError:
        pass
    return users
# End of home.py


