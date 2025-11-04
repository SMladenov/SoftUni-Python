#Hot Potato

listKids = input().split(' ')
toss = int(input())
startTossIndex = 0

while len(listKids) > 1:
    currentTossIndex = startTossIndex + (toss - 1)
    if currentTossIndex >= len(listKids):
        currentTossIndex %= len(listKids)
        #while currentTossIndex >= len(listKids):
        #    currentTossIndex -= len(listKids)
    print (f"Removed {listKids.pop(currentTossIndex)}")
    startTossIndex = currentTossIndex

print (f"Last is {listKids[0]}")
