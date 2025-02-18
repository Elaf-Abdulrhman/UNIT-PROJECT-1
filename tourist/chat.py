def ask_support():
    print("Welcome, how can I help you?")
    while True:
        message = input("Type 'e' to exit, 'c' to continue ").strip()
        if message == 'e':
            print("Exiting the support chat...")
            break
        elif message == 'c':
            print("Support: How can I help you? , choose from the list below")
            print("1. I need help with my account")
            print("2. I have a question about a destination")
            print("3. I want to report a bug")
            choice = input("Enter the number of your choice: ").strip()
            if choice == '1':
                print("do you want to reset your password? or do you want to delete your account?")
                if input == 'reset':
                    print("will be reseted once the function is added")
                elif input == 'delete':
                    print("will be deleted once the function is added")
            elif choice == '2':
                print("Support: I can help you with your destination question. Please provide more details.")
            elif choice == '3':
                print("Support: I can help you with reporting a bug. Please provide more details.")
            else:
                print("Support: I'm sorry, I didn't understand that choice.")
        
        
