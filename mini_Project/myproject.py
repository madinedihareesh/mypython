users = {}

def register():
    username = input("Enter your name: ")
    acc_no = input("Enter account number: ")
    password = input("Set your password: ")
    balance = float(input("Enter initial balance: "))

    users[acc_no] = {
        'username': username,
        'password': password,
        'balance': balance
    }
    print("Account created successfully!")

def login():
    acc_no = input("Enter account number: ")
    password = input("Enter password: ")

    user = users.get(acc_no)
    if user and user['password'] == password:
        print(f"Welcome back, {user['username']}!")
        perform_transactions(user)
    else:
        print("Invalid credentials!")

def perform_transactions(user):
    while True:
        print("\n1. Deposit\n2. Withdraw\n3. View Balance\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            user['balance'] += amount
            print("Deposited successfully. New Balance:", user['balance'])

        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            if amount <= user['balance']:
                user['balance'] -= amount
                print("Withdrawn successfully. New Balance:", user['balance'])
            else:
                print("Insufficient balance!")

        elif choice == '3':
            print("Your current balance is:", user['balance'])

        elif choice == '4':
            print("Logged out.\n")
            break

        else:
            print("Invalid choice!")

# Main Menu
while True:
    print("\n--- Welcome to Python Bank ---")
    print("1. Register\n2. Login\n3. Exit")
    option = input("Select an option: ")

    if option == '1':
        register()
    elif option == '2':
        login()
    elif option == '3':
        print("Thanks for visiting!")
        break
    else:
        print("Invalid option. Try again.")
1
