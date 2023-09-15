class BankAccount:
    def __init__(self, acc_number, acc_holder_name, initial_balance):
        self.__acc_number = acc_number
        self.__acc_holder_name = acc_holder_name
        self.__balance = initial_balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds!")

    def display_balance(self):
        print(f"Account Number: {self.__acc_number}")
        print(f"Account Holder: {self.__acc_holder_name}")
        print(f"Account Balance: {self.__balance}")


# Create an instance of BankAccount
account1 = BankAccount("1234567890", "John Doe", 1000)

# Test deposit and withdrawal functionality
account1.display_balance()

account1.deposit(500)
account1.display_balance()

account1.withdraw(200)
account1.display_balance()

account1.withdraw(1500)  # This should print "Insufficient funds!"
account1.display_balance()
