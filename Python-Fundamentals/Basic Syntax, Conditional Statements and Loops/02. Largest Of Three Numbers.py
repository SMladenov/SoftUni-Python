import sys

minInt = -sys.maxsize

for i in range (0, 3):
    num1 = int(input())
    if minInt < num1:
        minInt = num1

print (minInt)
