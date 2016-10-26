
class Operation(object):
    def __init__(self, amount, date):
        self.amount = amount
        self.date = date

    def __eq__(self, other):
        return (self.amount == other.amount) and (self.date == other.date)
