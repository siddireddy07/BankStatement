class Account():
    def __init__(self, username, password):
        self.username = username
        self.password = password
    def checkpassword(self, password):
        return self.password == password

class Operation():
    def __init__(self, avl_balance, withdraw_amount, deposit_amount):
        self.avl_balance = avl_balance
        self.withdraw_amount = withdraw_amount
        self.deposit_amount = deposit_amount
    
    def display_info(self):
        print("---------------")
        print(f"avl_balance: {self.avl_balance}")
        print(f"withdraw_amount: {self.withdraw_amount}")
        print(f"deposit_amount: {self.deposit_amount}")

accounts = []
loginaccount = None
while True:
    print("-----------------")
    print("\nWelcome to xbank. Please select the option to be processed:\n")
    print("-----------------")
    print("1. Create account\n2. Login\n3. Help")
    option = input("Enter the option to be processed: ")

    if not option:
        raise ValueError("Option cannot be empty")

    option = int(option)
    
    if option == 1:
        Firstname = input("Enter your first name: ")
        lastname = input("Enter your last name: ")
        c_number = input("Enter your contact number: ")
        username = input("Enter the username: ")
        password = input("Enter the password: ")
        if not (Firstname and lastname and c_number and username and password):
            raise ValueError("All fields must be filled")
        if len(c_number) != 10 or not c_number.isdigit():
            raise ValueError("Invalid Phone Number")
        accounts.append(Account(username, password))
        print("Account was created successfully. Please login with your credentials:")
    elif option == 2:
        username = input("Enter the username: ")
        password = input("Enter the password: ")
        if not (username and password):
            raise ValueError("Username and password cannot be empty")
        for account in accounts:
            if account.username == username and account.checkpassword(password):
                loginaccount = account
                print(f"{username} has logged in successfully")
                break
        if loginaccount is None:
            print("Invalid username or password")
        else:
            print("Bank Services:")
            break
    elif option == 3:
        print("Please contact the helpline number \"1800112233\" ")
        break
    else:
        print("Invalid details")  

balance = 25000
operations = []  # Store operation details

while True:
    if loginaccount is not None:
        print("\nWelcome to xbank")
        print("1. Balance enquiry")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Mini Statement")
        print("5. exit")
        option = input("Enter the option: ")

        if not option:
            raise ValueError("Option cannot be empty")

        option = int(option)

        if option == 1:
            print("Your balance is:", balance, "rs/-")
        elif option == 2:
            w_amount = input("Enter withdraw amount: ")
            if not w_amount:
                raise ValueError("Withdraw amount cannot be empty")
            w_amount = int(w_amount)
            if w_amount <= balance:
                balance = balance - w_amount
                print("Your updated balance is:", balance)
                operations.append(Operation(balance, w_amount, 0))
            else:
                print("Insufficient balance")
        elif option == 3:
            d_amount = input("Enter deposit amount: ")
            if not d_amount:
                raise ValueError("Deposit amount cannot be empty")
            d_amount = int(d_amount)
            print("Your previous balance is:", balance)
            balance = balance + d_amount
            print("Your updated balance is:", balance)
            operations.append(Operation(balance, 0, d_amount))
        elif option == 4:
            print("Mini Statement:")
            for op in operations:
                op.display_info()
                print("-------ThankYou-------")
                
        elif option == 5:
            print("exit\n")
            print("Thank you for choosing xbank as your banking partner")
            print("               ")
            break
        else:
            print("Please select a valid option")