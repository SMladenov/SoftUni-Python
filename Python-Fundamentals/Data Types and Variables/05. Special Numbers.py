#Special Numbers

number = int(input())

for i in range (1, number + 1):
    tempSum = 0
    strCast = str(i)
    for b in strCast:
        intTemp = int(b)
        tempSum += intTemp
    if tempSum == 5 or tempSum == 7 or tempSum == 11:
        print (f"{i} -> True")
    else:
        print (f"{i} -> False")
        