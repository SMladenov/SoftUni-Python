#Min Max and Sum

def MinMaxSum (numbers):
    minNumber = min(numbers)
    maxNumber = max(numbers)
    sumNumbers = sum(numbers)
    return f"The minimum number is {minNumber}\nThe maximum number is {maxNumber}\nThe sum number is: {sumNumbers}"
    
numbers = input()
numbersInt = [int(i) for i in numbers.split(' ')]

print (f"{MinMaxSum(numbersInt)}")
