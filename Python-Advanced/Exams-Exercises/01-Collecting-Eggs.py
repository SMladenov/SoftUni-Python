#Collecting Eggs

eggSize = [int(i) for i in input().split(', ')]
paperSize = [int(i) for i in input().split(', ')]

filledBoxes = 0
boxSize = 50

while eggSize and paperSize:
    currentEgg = eggSize[0]
    currentPaper = paperSize[-1]
    
    if currentEgg <= 0:
        eggSize.pop(0)
        continue
    elif currentEgg == 13:
        eggSize.pop(0)
        firstPaper = paperSize[0]
        paperSize[-1] = firstPaper
        paperSize[0] = currentPaper
        continue

    sumBoth = currentEgg + currentPaper

    if sumBoth <= boxSize:
        filledBoxes += 1
        eggSize.pop(0)
        paperSize.pop()
    else:
        eggSize.pop(0)
        paperSize.pop()
    
if filledBoxes > 0:
    print (f"Great! You filled {filledBoxes} boxes.")
else:
    print (f"Sorry! You couldn't fill any boxes!")

if eggSize:
    print (f"Eggs left: {', '.join(map(str, eggSize))}")
if paperSize:
    print (f"Pieces of paper left: {', '.join(map(str, paperSize))}")
