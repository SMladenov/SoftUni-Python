#Multiples List

num1 = int(input())
multiple = int(input())
valueToAppend = num1

listFinal = []

for i in range (multiple):
    listFinal.append(valueToAppend)
    valueToAppend += num1

print (listFinal)
