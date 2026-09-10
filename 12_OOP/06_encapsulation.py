# ============================================================
# ENCAPSULATION
# ============================================================
# Encapsulation means wrapping data and methods together inside
# a class and controlling access to the data.
#
# Python commonly uses:
#
# public       → name
# protected    → _name
# private      → __name
# ============================================================


class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

account = BankAccount(1000)
print(account.get_balance())
account.deposit(500)
print(account.get_balance())