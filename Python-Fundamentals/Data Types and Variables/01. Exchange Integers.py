#Exchange Integers

def exchangeIntegers (num1, num2):
    return f"Before:\na = {num1}\nb = {num2}\nAfter:\na = {num2}\nb = {num1}"

num1 = int(input())
num2 = int(input())

print (f"{exchangeIntegers(num1, num2)}")
