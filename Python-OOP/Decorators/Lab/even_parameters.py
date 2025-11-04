def even_parameters(function):
    def wrapper(*args, **kwargs):
        for el in args:
            if not isinstance(el, int):
                return f"Please use only even numbers!"
        oddList = [el for el in args if el % 2 == 1]
        if oddList:
            return f"Please use only even numbers!"
        else:
            result = function(*args, **kwargs)
            return result
    return wrapper




@even_parameters

def add(a, b):

    return a + b


print(add(2, 4))

print(add("Peter", 1))

@even_parameters

def multiply(*nums):

    result = 1

    for num in nums: 
        result *= num 
    return result 
print(multiply(2, 4, 6, 8)) 
print(multiply(2, 4, 9, 8))