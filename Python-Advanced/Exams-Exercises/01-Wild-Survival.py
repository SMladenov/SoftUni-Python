#Wild Survival

bees = [int(i) for i in input().split()]
beeEaters = [int(i) for i in input().split()]

while bees and beeEaters:
    currentBee = bees[0]
    currentEater = beeEaters[-1]

    if currentBee == currentEater * 7:
        bees.pop(0)
        beeEaters.pop()
    else:
        beeEatersNeeded = currentBee // 7
        if beeEatersNeeded < currentEater:
            beeEaters[-1] -= beeEatersNeeded
            bees.pop(0)
        else:
            survivedBees = currentBee - (currentEater * 7)
            beeEaters.pop()
            if len(bees) > 1:
                bees.pop(0)
                bees.append(survivedBees)
            else:
                bees[0] = survivedBees


print (f"The final battle is over!")
if not bees and not beeEaters:
    print (f"But no one made it out alive!")
if bees and not beeEaters:
    print (f"Bee groups left: {', '.join(map(str, bees))}")
if not bees and beeEaters:
    print (f"Bee-eater groups left: {', '.join(map(str, beeEaters))}")
