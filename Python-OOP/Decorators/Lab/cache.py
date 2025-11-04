def cache (func):
    log = {}

    def wrapper(*args):
        if args[0] in log:
            return log[args[0]]
        
        result = func(*args)
        log[args[0]] = result
        return result
    
    wrapper.log = log
    return wrapper
    


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci (n - 1) + fibonacci (n - 2)

# fibonacci(3)

# print(fibonacci.log)

fibonacci(4)

print(fibonacci.log)