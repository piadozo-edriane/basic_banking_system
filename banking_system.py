import os

class Bank:
    list_account = []

    def __init__(self, name, pin, balance):
        self.name = name
        self.pin = pin
        self.balance = balance

    def create_account ():
        user_name = input("Enter your name: ")
        user_pin = input("Enter your pin number: ")
        user_balance = 0
        
        account = Bank(user_name, user_pin, user_balance)
        Bank.list_account.append(account)

    def show_information (self):
        print (f"Your username is: {self.name}")
        print (f"Your user pin is: {self.pin}")
        print (f"Your current balance is: {self.balance}")

    def show_seperate_information ():
        if not Bank.list_account:
            print ("Account not found")
            return

        choice_account = int(input("Enter your account number: "))
        Bank.list_account[choice_account].show_information()        
        
    def display_created_account ():
        print ("The list of registered account")
        for account in Bank.list_account:
            account.show_information()
            print ("-" * 20)
    
    def account_checker ():
        check_name = input("Enter the username of your account: ")
        for account in Bank.list_account:
            if check_name == account.name:
                print ("Account is Existed")
                return

            print ("Account not existed")

    def balance_checker (self):
        user_decision = input("Do you want to contineu Y/N: ")
        print (f"Your current balance is: {self.balance}")

        if user_decision == "N":
            print ("Thanks")
            return
        print ("W for withdraw / D for deposit")
        input_user = input("Enter your choice: ")
        input_balance = int(input("The amount of money: "))

    def balance_user_display ():
        if not Bank.list_account:
            print ("Account not found")
            return

        choice_account = int(input("Enter your account number: "))
        Bank.list_account[choice_account].balance_checker()

    def deposit_balance (self, input_user, input_balance):
        if input_user == "D":
            self.balance += input_balance
            print (f"Your total balance is: {self.balance}")

    def deposit_balance_display (self):
        if not Bank.list_account:
            print ("Account not found")
            return

        choice_account = int(input("Enter your account number: "))
        Bank.list_account[choice_account].deposit_balance()

    def withdraw_balance (self, input_user, input_balance):
        if self.balance == 0:
            print (f"Can't withdraw you have: {self.balance}")
            return
        
        if input_user == "W":
            self.balance -= input_balance
            print (f"Your current balance is: {self.balance}")
    
    def withdraw_balance_display ():
        if not Bank.list_account:
            print ("Account not found")
            return

        choice_account = int(input("Enter your account number: "))
        Bank.list_account[choice_account].balance_checker()


while True:
    os.system ("cls")
    print ("1. Create account")
    print ("2. Show information account")
    print ("3. Display registered account")
    print ("4. Check account if registered")
    print ("5. Balance checker")
    print ("6. Deposit")
    print ("7. Withdraw")

    input_user = input ("Enter your choice: ")

    if input_user == "0":
        break

    match input_user:
        case "1":
            os.system("cls")
            Bank.create_account()
            input ()
        case "2":
            os.system("cls")
            Bank.show_seperate_information()
            input ()
        case "3":
            os.system("cls")
            Bank.display_created_account()
            input ()
        case "4":
            os.system("cls")
            Bank.account_checker()
            input()
        case "5":
            os.system("cls")
            Bank.balance_user_display()
            input
        case _:
            print ("Invalid choice")
