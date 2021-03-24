from abc import ABC

from account_func import Account


class SavingsAccount(Account, ABC):

    def refresh(self, rate):
        self.__balance += self.__balance * rate * 3
