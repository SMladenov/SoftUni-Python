#Smallest of Three Numbers

import math

def findSmallest (num1, num2, num3):
    return min((min(num1, num2)), num3)

num1 = int(input())
num2 = int(input())
num3 = int(input())

print (f"{findSmallest(num1, num2, num3)}")
