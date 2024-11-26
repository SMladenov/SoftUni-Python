#Letters Change Numbers

wholeStrings = input().split(' ')
wholeStrings = [i.strip() for i in wholeStrings if i.strip()]

totalSum = 0

for i in wholeStrings:
    number = ""
    alphaBefore = ""
    alphaAfter = ""
    for b in range (0, len(i) - 1):
        if i[b].isdigit():
            if i[b-1].isalpha():
                alphaBefore += i[b-1]
            number += i[b]
            if i[b + 1].isalpha():
                alphaAfter += i[b+1]

    #print (f"{number}\n{alphaBefore}\n{alphaAfter}")
    
    number = int(number)
    if alphaBefore.isupper():
        position = ord(alphaBefore) - 64
        tempOperation = number / position
        if alphaAfter.isupper():
            result = tempOperation - (ord(alphaAfter) - 64)
            totalSum += result
        if alphaAfter.islower():
            result = tempOperation + (ord(alphaAfter.upper()) - 64)
            totalSum += result
    if alphaBefore.islower():
        position = ord(alphaBefore.upper()) - 64
        tempOperation = number * position
        if alphaAfter.isupper():
            result = tempOperation - (ord(alphaAfter) - 64)
            totalSum += result
        if alphaAfter.islower():
            result = tempOperation + (ord(alphaAfter.upper()) - 64)
            totalSum += result
    
print (f"{totalSum:.2f}")