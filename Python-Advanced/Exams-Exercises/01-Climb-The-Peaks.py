#Climb The Peaks

food = [int(i) for i in input().split(', ')]
stamina = [int(i) for i in input().split(', ')]


tupleMounts = [("Vihren", 80), ("Kutelo", 90), ("Banski Suhodol", 100), ("Polezhan", 60), ("Kamenitza", 70)]
peaksToPrint = []

conqueredPeaks = 0

while food and stamina:
    currentFood = food[-1]
    currentStamina = stamina[0]
    sumBoth = currentFood + currentStamina

    currentMountTarget = tupleMounts[0]
    difficulty = currentMountTarget[1]

    if sumBoth >= difficulty:
        conqueredPeaks += 1
        tupleMounts.pop(0)
        peaksToPrint.append(currentMountTarget[0])
        food.pop()
        stamina.pop(0)
    else:
        food.pop()
        stamina.pop(0)

    if conqueredPeaks == 5:
        break

if conqueredPeaks == 5:
    print (f"Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
    print (f"Conquered peaks:")
    for peak in peaksToPrint:
        print (f"{peak}")
else:
    print (f"Alex failed! He has to organize his journey better next time -> @PIRINWINS")
    if conqueredPeaks > 0:
        print (f"Conquered peaks:")
        for peak in peaksToPrint:
            print (f"{peak}")
