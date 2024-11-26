#Josephus Permutation

import sys

randomStr = input().split(' ')
jump = int(input())

newList = []

currentJump = jump
counter = 0
originalLength = len(randomStr)

while counter < originalLength:
    if currentJump > len(randomStr):
        while currentJump > len(randomStr):
            currentJump -= len(randomStr)
    newList.append(randomStr[currentJump - 1])
    randomStr.pop(currentJump - 1)
    counter += 1
    currentJump += jump - 1

print (f"[{','.join(newList)}]")
