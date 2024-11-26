firstInput = input().split('|')
secondFormat = []

for i in firstInput:
    eventValue = i.split('-')
    secondFormat.append(eventValue[0])
    secondFormat.append(eventValue[1])

coins = 100
energy = 100
dayManaged = True

for i in range (0, len(secondFormat) - 1, + 2):
    event = secondFormat[i]
    value = float(secondFormat[i + 1])
    if event == "rest":
        energy += value
        if energy > 100:
            energy = 100
            print (f"You gained {round((energy - 100))} energy.\nCurrent energy: {round(energy)}.")
        else:
            print(f"You gained {round(value)} energy.\nCurrent energy: {round(energy)}.")
    elif event == "order":
        energyLeft = energy - 30
        if energyLeft >= 0:
            energy -= 30
            coins += value
            print (f"You earned {round(value)} coins.")
        else:
            energy += 50
            print ("You had to rest!")
    else:
        coinsLeft = coins - value
        if coinsLeft >= 0:
            coins -= value
            print (f"You bought {event}.")
        else:
            print (f"Closed! Cannot afford {event}.")
            dayManaged = False
            break

if dayManaged:
    print (f"Day completed!\nCoins: {round(coins)}\nEnergy: {round(energy)}")
    