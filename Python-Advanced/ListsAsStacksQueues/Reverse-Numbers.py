#Reverse Numbers
#Stack

inputStr = [int(i) for i in input().strip().split(' ') if i.strip()]
toPrint = []
while inputStr:
    toPrint.append(inputStr.pop())

print (" ".join(map(str, toPrint)))