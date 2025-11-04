#Longest Intersection

numberIntersections = int(input())

longestInterList = []
longestInter = 0

for _ in range (numberIntersections):
    currentInterLong = 0
    currentInter = []
    interSplit = input().split('-')
    inter1 = [int(i) for i in interSplit[0].split(',')]
    inter2 = [int(i) for i in interSplit[1].split(',')]

    #First Range
    if inter1[0] >= inter2[0]:
        currentInter.append(inter1[0])
    if inter2[0] > inter1[0]:
        currentInter.append(inter2[0])
    #Second Range
    if inter1[1] <= inter2[1]:
        currentInter.append(inter1[1])
    if inter2[1] < inter1[1]:
        currentInter.append(inter2[1])

    #Calculating longest intersection with index inclusive
    currentInterLong = (currentInter[1] + 1) - currentInter[0]
    if longestInter < currentInterLong:
        longestInter = currentInterLong
        longestInterList = currentInter.copy()

listToBePrinted = [str(i) for i in range (longestInterList[0], longestInterList[1] + 1)]

print (f"Longest intersection is [{', '.join(listToBePrinted)}] with length {longestInter}")