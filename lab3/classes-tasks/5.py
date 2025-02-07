class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("$",amount,"deposited. New balance: $",self.balance)
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds. Current balance: $",self.balance)
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print("$",amount,"withdrawn. New balance: $",self.balance)

    def __str__(self):
        return "Account Owner:",self.owner ,"\nAccount Balance: $",self.balance

acct = Account("Yerbolat", 100)

print(acct)

acct.deposit(50)
acct.withdraw(30)
acct.withdraw(150)
acct.withdraw(-10)
