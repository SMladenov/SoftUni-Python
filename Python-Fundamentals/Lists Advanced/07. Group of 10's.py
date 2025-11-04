#Group of 10's

numList = [int(i) for i in input().split(', ')]

listTemp = []

startGroup = 0
endGroup = 10

while len(numList) > 0:
    for i in numList:
        if startGroup < i <= endGroup:
            listTemp.append(i)
    numList = [i for i in numList if i not in listTemp]
    print (f"Group of {endGroup}'s: {listTemp}")
    startGroup += 10
    endGroup += 10
    listTemp.clear()
    