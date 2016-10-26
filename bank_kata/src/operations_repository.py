class OperationsRepository(object):
    def __init__(self):
        self.operations = []

    def add(self, operation):
        self.operations.append(operation)

    def deposits(self):
        return filter(lambda o: o.amount > 0, self.operations)
