#Messaging

randomNums = input().split(' ')
randomStr = input()

finalStr = ""

for i in randomNums:
    index = 0
    for b in i:
        intParse = int(b)
        index += intParse
    if index >= len(randomStr):
        while index >= len(randomStr):
            index -= len(randomStr)
    if index <= len(randomStr) - 1:
        finalStr += randomStr[index]
        randomStr = randomStr[:index] + randomStr[index + 1:]

print (f"{finalStr}")
