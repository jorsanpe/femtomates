from bank_account import BankAccount
from statement_formatter import format_operations


class BankLibrary(object):
    def set_up(self):
        self.account = BankAccount()
        self.printed_text = ''

    def deposit(self, amount, on, date):
        self.account.deposit(int(amount), date)

    def withdraw(self, amount, on, date):
        self.account.withdraw(int(amount), date)

    def print_statements(self):
        operations = self.account.operations()
        self.printed_text = format_operations(operations)

    def print_deposits(self):
        deposits = self.account.deposits()
        self.printed_text = format_operations(deposits)

    def get_printed_statements(self):
        return self.printed_text

