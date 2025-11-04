#Odd and Even Sum

def sumOfAllEvenAndOdd (num1):
    sumEven = 0
    sumOdd = 0
    for i in num1:
        intParse = int(i)
        if intParse % 2 == 0:
            sumEven += intParse
        else:
            sumOdd += intParse
    return f"Odd sum = {sumOdd}, Even sum = {sumEven}"

num1 = input()

print (f"{sumOfAllEvenAndOdd(num1)}")
