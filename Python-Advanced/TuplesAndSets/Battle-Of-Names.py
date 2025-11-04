#Battle of Names

numberNames = int(input())

oddSet = set()
evenSet = set()

for _ in range (1, numberNames + 1):
    name = input()
    sumChars = 0
    for i in name:
        sumChars += ord(i)
    sumChars //= _
    if sumChars % 2 == 0:
        evenSet.add(sumChars)
    else:
        oddSet.add(sumChars)

if sum(evenSet) > sum(oddSet):
    print (f"{', '.join(map(str, oddSet.symmetric_difference(evenSet)))}")
if sum(evenSet) == sum(oddSet):
    print (f"{', '.join(map(str, oddSet.union(evenSet)))}")
if sum(oddSet) > sum(evenSet):
    print (f"{', '.join(map(str, oddSet.difference(evenSet)))}")
