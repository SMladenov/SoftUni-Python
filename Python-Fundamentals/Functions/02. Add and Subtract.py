#Add and Subtract

import math

def sum_numbers(num1, num2):
    return num1 + num2

def subtract(result, num3):
    return result - num3
    
num1 = int(input())
num2 = int(input())
num3 = int(input())

sum = sum_numbers(num1, num2)
sub = subtract(sum, num3)

print (sub)
