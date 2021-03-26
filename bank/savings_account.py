from account_func import Account


class SavingsAccount(Account):

    def refresh(self, rate):
        self.__balance += self.__balance * rate * 3
