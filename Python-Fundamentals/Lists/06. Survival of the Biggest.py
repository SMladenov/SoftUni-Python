#Survival of the Biggest

import sys

listInts = input().split(' ')
numbers = int(input())

for i in range(numbers):
    tempNum = sys.maxsize
    for b in listInts:
        intParse = int(b)
        if intParse < tempNum:
            tempNum = intParse
    listInts.remove(str(tempNum))
    tempNum = sys.maxsize

print (f"{', '.join(listInts)}")
