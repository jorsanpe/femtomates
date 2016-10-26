# date || amount || balance
# 10 - 01 - 2012 || 1000 || 1000


def format_operations(operations):
    text = 'date || amount || balance\n'
    balance = 0
    for o in operations:
        balance += o.amount
        text += '%s || %d || %d' % (o.date, o.amount, balance)
    return text
