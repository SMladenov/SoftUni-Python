#Number Beggars

stringInts = input()
listInts = stringInts.split(', ')

beggars = int(input())

if beggars > len(listInts):
    tempList = []
    for i in listInts:
        tempList.append(i)
    for i in range (0, (beggars - len(listInts))):
        tempList.append('0')
    print (f"[{', '.join(tempList)}]")

if beggars == len(listInts):
    print (f"[{', '.join(listInts)}]")

if beggars < len(listInts):
    tempList = []
    for i in range (0, beggars):
        tempSum = 0
        for b in range (i, len(listInts), +beggars):
            tempSum += int(listInts[b])
        tempList.append(str(tempSum))
        tempSum = 0
    print (f"[{', '.join(tempList)}]")
    