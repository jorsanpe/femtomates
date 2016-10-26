class OperationsRepository(object):
    def __init__(self):
        self.operations = []

    def add(self, operation):
        self.operations.append(operation)