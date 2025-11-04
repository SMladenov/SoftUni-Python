#Social Distribution

population = [int(i) for i in input().split(', ')]
minWealth = int(input())

leftWealth = 0
isDistributed = True

while min(population) < minWealth:
    maxElement = max(population)
    indexMax = population.index(maxElement)
    minElement = min(population)
    indexMin = population.index(minElement)

    if maxElement == minWealth and minElement < minWealth:
        print(f"No equal distribution possible")
        isDistributed = False
        break
    else:
        neededAmount = minWealth - minElement
        tempAmount = 0
        if (maxElement - neededAmount) >= minWealth:
            population[indexMax] -= neededAmount
            population[indexMin] += neededAmount
        else:
            tempAmount += (maxElement - minWealth)
            population[indexMax] = minWealth
            population[indexMin] += tempAmount
            

if isDistributed:
    print (f"{population}")
    