class Account:
    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance

    def deposit(self, amount):
        self.balance +=  amount
        print(self)

    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
            print(self)
        else:
            print("Sorry, not enough funds!")
            print(self)

    def transfer(self, another, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
            another.balance += amount
            print(self)
        else:
            print("Sorry, not enough funds!")
            print(self)

    def statement(self):
        print("Account Balance: ${}".format(self.balance))

    def __del__(self):
        print("Account Closed!")

class Current(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = -1000 )

    def __str__(self):
        return "{}'s Current Account : Balance ${}".format(self.name, self.balance)

class Savings(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = 0)

    def __str__(self):
        return "{}'s Savings Account : Balance ${}".format(self.name, self.balance)

    
