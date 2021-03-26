from account_func import Account


class CheckingAccount(Account):

    def refresh(self, rate):
        self.__balance += self.__balance * rate * 2
