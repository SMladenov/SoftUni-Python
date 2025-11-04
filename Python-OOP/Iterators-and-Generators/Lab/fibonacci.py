def fibonacci():
    a, b = 0, 1 
    while True: 
        yield a  
        a, b = b, a + b 

generator = fibonacci()

# for i in range(5):

#     print(next(generator))

# generator = fibonacci()

# for i in range(1):

#     print(next(generator))

def read_next(*args):
    for iterable in args:
        for item in iterable:
            yield item

# for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):

#     print(item, end='')

# for i in read_next("Need", (2, 3), ["words", "."]): 
    
#     print(i)

from math import sqrt

def get_primes(listNums: list):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    for num in listNums:
        if is_prime(num):
            yield num

print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
      
print(list(get_primes([-2, 0, 0, 1, 1, 0])))