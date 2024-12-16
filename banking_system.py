import os

class BankAccount:
    def __init__(self, name, pin, age, gender, balance):
        self.name = name
        self.pin = pin
        self.age = age
        self.gender = gender
        self.balance = balance

    def account_holder (self):
        print (f"Your name is: {self.name}")
        print (f"You pin is: {self.pin}")
        print (f"Your age is: {self.age}")
        print (f"Your gender is: {self.gender}")
        print (f"Your current balance is: {self.balance}")
        
    global list_account

    list_account = []

    def input_account (self):
        os.system("cls")
        num_of_account = int(input("Enter the number of account you want to add: "))
        for num in range (num_of_account):
            print (f"Account number {num + 1}")
            name = str(input("Enter your name: "))
            pin = int(input("Enter your pin number: "))
            age = int(input("Enter your age: "))
            gender = str(input("Enter your gender: "))
            account = BankAccount(name, pin, age, gender) 
            list_account.append(account)

    def display_account(self):
        print ("The list of account")
        for num in list_account:
            num.account_holder()
            print ("+" * 20)

    def account_checker (self):
        os.system("cls")
        user_name = str(input("Enter the name of your account: "))
        for account in list_account:
            if account.name == user_name:
                print ("Access granted")
                return
            
        print ("Your account did'nt exist")

    def balance (self):
        self.balance = 0
        user_pin = int(input("Enter your pin to your account: "))
        for account in list_account:
            if account.pin == user_pin:
                choice = input ("D for deposit, W for withdraw")
                if choice == "D":
                    deposit = int(input("Enter the amount you want to deposist: "))
                    self.balance += deposit
                if self.balance == 0:
                    print ("You can't withdraw")
                    if choice == "W":
                        withdraw_ammount = int(input("Enter the amount you want to withdraw: "))
                        self.balance -= withdraw_ammount

BankAccount.input_account ()
BankAccount.account_checker ()
BankAccount.account_checker ()