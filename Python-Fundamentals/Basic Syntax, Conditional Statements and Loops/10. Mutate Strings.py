#Mutate Strings

firstStr = input()
secondStr = input()

listUsedStrings = []
tempString = ""

for i in range (0, len(secondStr)):
    if firstStr[i] != secondStr[i]:
        tempString = secondStr[:i + 1] + firstStr[i + 1:]
        if tempString not in listUsedStrings:
            listUsedStrings.append(tempString)
for i in listUsedStrings:
    print (i)
