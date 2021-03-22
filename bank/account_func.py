class Account:
    def __init__(self, number, name, balance, limit):
        self.number = number
        self.name = name
        self.balance = balance
        self.limit = limit

    def display_balance(self):
        print("Account number:	{}	\nBalance:	{}".format(self.number, self.balance))

    def withdraw(self, value):
        if self.balance >= value:
            self.balance -= value
            return True

        return False

    def deposit(self, value):
        self.balance += value
        return True

    def transfer(self, value, account_number):
        withdrawed = self.withdraw(value)
        if withdrawed:
            account_number.deposit(value)
            return True
        else:
            return False
