#Longer Line

import math

def longerLine (listNums):
    listP = []
    for i in listNums:
        if i < 0:
            listP.append(i * -1)
        else:
            listP.append(i)
    
    listLeft = [listP[0], listP[1], listP[2], listP[3]]
    listRight = [listP[4], listP[5], listP[6], listP[7]]
    if sum(listLeft) < sum(listRight):
        firstPair = listRight[0] + listRight[1]
        secondPair = listRight[2] + listRight[3]
        if firstPair > secondPair:
            return f"({math.floor(listNums[6])}, {math.floor(listNums[7])})({math.floor(listNums[4])}, {math.floor(listNums[5])})"
        else:
            return f"({math.floor(listNums[4])}, {math.floor(listNums[5])})({math.floor(listNums[6])}, {math.floor(listNums[7])})"
    if sum(listRight) <= sum(listLeft):
        firstPair = listLeft[0] + listLeft[1]
        secondPair = listLeft[2] + listLeft[3]
        if firstPair > secondPair:
            return f"({math.floor(listNums[2])}, {math.floor(listNums[3])})({math.floor(listNums[0])}, {math.floor(listNums[1])})"
        else:
            return f"({math.floor(listNums[0])}, {math.floor(listNums[1])})({math.floor(listNums[2])}, {math.floor(listNums[3])})"

listNums = []

for i in range (8):
    number = float(input())
    listNums.append(number)

print (f"{longerLine(listNums)}")
