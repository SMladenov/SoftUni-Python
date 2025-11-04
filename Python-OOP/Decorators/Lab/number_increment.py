def number_increment(numbers):

    def increase():
        return [i + 1 for i in numbers]

    return increase()

# print(number_increment([1, 2, 3]))

def vowel_filter(function): 

    def wrapper(): 
        vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'u', 'U', 'y', 'Y', 'o', 'O']
        return [char for char in function() if char in vowels]

    return wrapper

@vowel_filter

def get_letters():

    return ["a", "b", "c", "d", "e"]


# print(get_letters())

def even_numbers(function):

    def wrapper(*args, **kwargs):
        numbersList = function(*args, **kwargs)
        return [num for num in numbersList if num % 2 == 0]
    return wrapper

@even_numbers
def get_numbers(numbers):
    return numbers

# print(get_numbers([1, 2, 3, 4, 5]))

def multiply(times):

    def decorator(function):
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs) * times
            return result

        return wrapper
    return decorator

@multiply(3)
def add_ten(number):
    return number + 10

print(add_ten(3))

