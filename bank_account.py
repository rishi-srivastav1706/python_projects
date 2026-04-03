class BankAccount:
    def __init__(self, account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")
    def display_balance(self):
        print("The balance is:", self.balance)
account1 = BankAccount("123456789", "John Doe", 1000)
account1.deposit(500)
account1.withdraw(200)
account1.display_balance()
