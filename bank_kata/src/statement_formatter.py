# date || amount || balance
# 10 - 01 - 2012 || 1000 || 1000


def format_operations(operations):
    text = 'date || amount || balance'
    balance = 0
    for o in reversed(operations):
        balance += o.amount
        text += '\n%s || %d || %d' % (o.date, o.amount, o.balance)
    return text
