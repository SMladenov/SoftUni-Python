#Factorial Division

def factorialDivision (num1, num2):
    factorial1 = num1
    factorial2 = num2
    for i in range (num1 - 1, 0, -1):
        factorial1 *= i
    for i in range (num2 - 1, 0, -1):
        factorial2 *= i
    return f"{(factorial1 / factorial2):.2f}"
    

num1 = int(input())
num2 = int(input())

print (f"{factorialDivision(num1, num2)}")
