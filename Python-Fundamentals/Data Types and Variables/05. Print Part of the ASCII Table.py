#Print Part of the ASCII Table

charsStart = int(input())
charsStop = int(input())

listChars = []

for i in range (charsStart, charsStop + 1):
    tempChar = chr(i)
    listChars.append(tempChar)

print (' '.join(listChars))
