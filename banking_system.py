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
                print ("Access granted")
            
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
                if account.balance_bank == 0:
                    print ("You can't withdraw")
                    print ("Your balance is zero")
                    if choice == "W":
                        withdraw_ammount = int(input("Enter the amount you want to withdraw: "))
                        account.balance_bank -= withdraw_ammount
                        print (f"your current balance is: {account.balance_bank}")

BankAccount.input_account()
BankAccount.account_checker ()
BankAccount.account_checker ()
BankAccount.balance()