class Account:
    _acc_qty = 0

    def __init__(self, number, name, balance, limit):
        self._number = number  # PROTECTED
        self._name = name
        self.__balance = balance  # PRIVATE
        self._limit = limit
        Account._acc_qty += 1  # Will increment the static value of number of accounts objects

    def __str__(self):
        return "Account info:	\nNumber:	{}	\nName:	{}	\nBalance:	{}	\nLimit:{}".format(
            self._number, self._name, self._limit, self.__balance)

    def get_balance(self):
        return self.__balance

    @property
    def number(self):
        return self._number

    @property
    def name(self):
        return self._name

    @property
    def limit(self):
        return self._limit

    def display_balance(self):
        print("Account number:	{}	\nBalance:	{}".format(self.number, self.get_balance()))

    def withdraw(self, value):
        if self.get_balance() >= value:
            self.__balance -= value
            return True

        return False

    def deposit(self, value):
        if value < 0:
            return False
        else:
            self.__balance += value - 0.1
            return True

    def transfer(self, value, account_number):
        withdrawed = self.withdraw(value)
        if withdrawed:
            account_number.deposit(value)
            return True
        else:
            return False

    def print_dir(self):
        print(dir(self))

    @property
    def acc_qty(self):
        return self._acc_qty

    @classmethod
    def get_acc_qty(cls):
        print(f'Accounts quantity: {cls.acc_qty}')

    def refresh(self, rate):
        self.__balance += self.__balance * rate

    #@property
    #@abc.abstractmethod
    #def acc_type(self):
    #    pass
