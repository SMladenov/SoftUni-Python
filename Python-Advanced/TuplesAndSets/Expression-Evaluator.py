#Expression Evaluator

import math
import sys
import operator

randomStr = [i for i in input().strip().split()]
dicOperators = {
    '*': operator.mul,
    '+': operator.add, 
    '-': operator.sub, 
    '/': operator.truediv
    }

tempList = []
tempSum = sys.maxsize

while randomStr:
    tempChar = randomStr.pop(0)
    if tempChar not in dicOperators.keys():
        tempList.append(int(tempChar))
    else:
        if tempChar != '/':
            if tempSum == sys.maxsize:
                tempSum = tempList[0]
                if len(tempList) > 1:
                    for i in range (1, len(tempList)):
                        tempSum = dicOperators.get(tempChar)(tempSum, tempList[i])
            else:
                #tempList.insert(0, tempSum)
                for i in range (0, len(tempList)):
                    tempSum = dicOperators.get(tempChar)(tempSum, tempList[i])

        else:
            if tempSum == sys.maxsize:
                tempSum = tempList[0]
                if len(tempList) > 1:
                    for i in range (1, len(tempList)):
                        tempSum = math.floor(dicOperators.get(tempChar)(tempSum, tempList[i]))
            else:
                #tempList.insert(0, tempSum)
                for i in range (0, len(tempList)):
                    tempSum = math.floor(dicOperators.get(tempChar)(tempSum, tempList[i]))

        tempList.clear()

print (f"{tempSum}")