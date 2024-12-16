import os

class BankAccount:
    global list_account

    list_account = []
    def __init__(self, name, pin, age, gender, balance_bank):
        self.name = name
        self.pin = pin
        self.age = age
        self.gender = gender
        self.balance_bank = balance_bank

    def account_holder (self):
        print (f"Your name is: {self.name}")
        print (f"You pin is: {self.pin}")
        print (f"Your age is: {self.age}")
        print (f"Your gender is: {self.gender}")
        print (f"Your current balance is: {self.balance_bank}")

    def input_account ():
        os.system("cls")
        num_of_account = int(input("Enter the number of account you want to add: "))
        for num in range (num_of_account):
            print (f"Account number {num + 1}")
            name = str(input("Enter your name: "))
            pin = int(input("Enter your pin number: "))
            age = int(input("Enter your age: "))
            gender = str(input("Enter your gender: "))
            balance_bank = 0
            account = BankAccount(name, pin, age, gender, balance_bank) 
            list_account.append(account)

    def display_account():
        print ("The list of account")
        for num in list_account:
            num.account_holder()
            print ("+" * 20)

    def account_checker ():
        os.system("cls")
        user_name = str(input("Enter the name of your account: "))
        for account in list_account:
            if account.name == user_name:
                print ("Account Exist")
                return
            
        print ("Your account did'nt exist")

    def balance ():
        os.system("cls")
        user_pin = int(input("Enter your pin to your account: "))
        for account in list_account:
            if account.pin == user_pin:
                choice = input ("D for deposit, W for withdraw: ")
                if choice == "D":
                    deposit = int(input("Enter the amount you want to deposist: "))
                    account.balance_bank += deposit
                    print (f"your current balance is: {account.balance_bank}")
                elif account.balance_bank <= 0:
                    print ("You can't withdraw")
                    print ("Your balance is zero")
                    return
                elif choice == "W":
                    withdraw_ammount = int(input("Enter the amount you want to withdraw: "))
                    account.balance_bank -= withdraw_ammount
                    print (f"your current balance is: {account.balance_bank}")
            elif account.pin != user_pin:
                print ("User pin is incorrect")
                return
        
    def transfer_balance ():
        for account in list_account:
            check_user = str(input("Enter your name: "))
            if account.name == check_user:
                transfer_balance = account.balance_bank
                transfer_user = str(input("Enter the name you want to transfer: "))
                transfer_balance = int(input("Enter the amount you want to transfer: "))
                account.balance_bank -= transfer_balance
                print (f"Your total balance is: {account.balance_bank}")

            if account.name == transfer_user:
                account.balance_bank += transfer_balance
                print (f"Your total balance is: {account.balance_bank}")

while True:
    os.system("cls")
    print ("1. Input account")
    print ("2. Display account")
    print ("3. Account checker")
    print ("4. Deposit and Withdraw checker")
    print ("5. Transfer to another user")
    print ("6. Exit")    
    choice = input("Enter your choice: ")

    if choice == "6":
        break
    match choice: 
        case "1":
            os.system("cls")
            BankAccount.input_account()
            input()
        case "2":
            os.system("cls") 
            BankAccount.display_account()
            input()
        case "3":
            os.system("cls")
            BankAccount.account_checker()
            input()
        case "4":
            os.system("cls")
            BankAccount.balance()
            input()
        case "5":
            BankAccount.transfer_balance()
            input()
        case _:
            print ("Invalid choice")