#Set of Elements

setNums1 = set()
setNums2 = set()

lengthSet = [int(i) for i in input().split()]
for _ in range (lengthSet[0]):
    setNums1.add(int(input()))
for _ in range (lengthSet[1]):
    setNums2.add(int(input()))

equalSet = (setNums1 & setNums2)
print (*equalSet, sep='\n')