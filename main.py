# Virtual ATM System for Teens

# Step 1: Sample user accounts as list of tuples (Name, PIN, Balance)

users= [
    ("Jack", "1234", 100000),
    ("Abdullah", "2011", 1200000),
    ("Ibrahim", "0000", 10000),
]

# Step 2: Empty transaction logs (for each user) - use nested lists

transaction_logs = [
    [],[],[] 
]  

# Step 3: Login function with while loop
#         Give user specific number of attempts to enter name and pin before quitting.
#         Return the index of user logging in.
def login():
    print("\n Welcome to Virtual ATM")
    attempts = 0
    while attempts < 3:
        name = input(" Enter your name: ")
        pin = input(" Enter your 4-digit PIN: ")

        for user in range(len(users)):
            if users[user][0].lower() == name and users[user][1] == pin:
                print("\n Login successful.")
                return user 
    
        print(" Incorrect name or PIN. Try again.")
        attempts += 1
        print(" Too many failed attempts. Exiting the atm...")
        return None
    
    ...

# Step 4: ATM Menu (main loop)
# Provide options to check balance, deposit, withdraw, and show mini statement.
def atm_menu(user_index):
    ...
    while True:
        print("\n=====  ATM Menu =====")
        print("Enter 1 to Check Balance")
        print("Enter 2 to Deposit Money")
        print("Enter 3 to Withdraw Money")
        print("Enter 4 to Mini Statement")
        print("Enter 5 to Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
             print(f"\n Your current balance is Rs. {users[user_index][2]}")

        elif choice == "2":
            amount_to_deposit = int(input("Enter amount to deposit: Rs. "))
            users[user_index] = (
            users[user_index][0],
            users[user_index][1],
            users[user_index][2] +   amount_to_deposit
                        )
            transaction_logs[user_index].append(f"Deposited Rs. { amount_to_deposit}")
            print(" Deposit successful.")
        elif choice == "3":
            withdraw_amount = int(input("Enter amount to withdraw: Rs. "))
            if withdraw_amount <= users[user_index][2]:
                            users[user_index] = (
                                users[user_index][0],
                                users[user_index][1],
                                users[user_index][2] - withdraw_amount
                            )
                            transaction_logs[user_index].append(f"Withdrew Rs. {withdraw_amount}")
                            print(" Withdrawal successful.")
            else:
                print(" Insufficient balance.")


# Step 5: Run program by calling functions in appropriate order


user_index = login()
if user_index is not None:
    atm_menu(user_index)




