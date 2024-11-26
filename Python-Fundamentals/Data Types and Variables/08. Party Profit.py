#Party Profit
import math

groupSize = int(input())
days = int(input())

daysCounter = 0
coins = 0


while days > 0:
    days -= 1
    daysCounter += 1

    if daysCounter % 10 == 0:
        groupSize -= 2
    if daysCounter % 15 == 0:
        groupSize += 5
        
    coins += 50
    coins -= (2 * groupSize)
    
    if daysCounter % 3 == 0:
        coins -= (3 * groupSize)
    if daysCounter % 5 == 0:
        if daysCounter % 3 == 0:
            coins -= (2 * groupSize)
        coins += (20 * groupSize)

print (f"{groupSize} companions received {math.floor(coins / groupSize)} coins each.")
