from bank_account import BankAccount
from statement_formatter import format_operations


class BankLibrary(object):
    def __init__(self):
        self.account = BankAccount()

    def deposit(self, amount, on, date):
        self.account.deposit(int(amount), date)

    def print_statements(self):
        operations = self.account.operations()
        return format_operations(operations)
 