
class Operation(object):
    def __init__(self, amount, date, balance):
        self.amount = amount
        self.date = date
        self.balance = balance

    def __eq__(self, other):
        return (self.amount == other.amount) and (self.date == other.date) and (self.balance == other.balance)
