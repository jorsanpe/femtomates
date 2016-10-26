from operation import Operation
from operations_repository import OperationsRepository


class BankAccount(object):
    def __init__(self):
        self.amount = 0
        self.operations_repository = OperationsRepository()

    def deposit(self, amount, date):
        self.amount += amount
        self.operations_repository.add(Operation(amount, date))

    def print_statements(self):
        pass

    def balance(self):
        return self.amount

    def operations(self):
        return self.operations_repository.operations
