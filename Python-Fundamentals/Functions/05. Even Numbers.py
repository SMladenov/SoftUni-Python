#Even numbers

def isEven(num):
    if num % 2 == 0:
        return True

numbers = input().split(' ')
numbersInt = [int(i) for i in numbers]

evenNumbers = filter(isEven, numbersInt)

print (list(evenNumbers))
