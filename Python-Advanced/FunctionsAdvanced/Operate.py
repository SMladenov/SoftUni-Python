#Operate

from functools import reduce

def operate (operator, *args):

    def multiplication():
        return reduce(lambda x, y: x * y, args)
    def subtract():
        return reduce(lambda x, y: x - y, args)
    def add():
        return reduce(lambda x, y: x + y, args)
    def division():
        return reduce(lambda x, y: x / y, args)

    dictOperator = {
        '*': multiplication(), 
        '-': subtract(),
        '+': add(),
        '/': division()
    }

    return dictOperator.get(operator)