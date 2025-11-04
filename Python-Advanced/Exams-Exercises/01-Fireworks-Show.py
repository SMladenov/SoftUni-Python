#Fireworks Show

effects = [int(i) for i in input().split(', ')]
power = [int(i) for i in input().split(', ')]

palmFirework = 0
willowFirework = 0
crossetteFirework = 0
enoughFirework = False


while effects and power:
    currentEffect = effects[0]
    currentPower = power[-1]

    fireworkMade = False
    
    if currentEffect <= 0:
        effects.pop(0)
        continue
    elif currentPower <= 0:
        power.pop()
        continue
    
    sumOfBoth = currentEffect + currentPower
    if sumOfBoth % 3 == 0 and sumOfBoth % 5 != 0:
        palmFirework += 1
        effects.pop(0)
        power.pop()
        fireworkMade = True
    elif sumOfBoth % 3 != 0 and sumOfBoth % 5 == 0:
        willowFirework += 1
        effects.pop(0)
        power.pop()
        fireworkMade = True
    elif sumOfBoth % 3 == 0 and sumOfBoth % 5 == 0:
        crossetteFirework += 1
        effects.pop(0)
        power.pop()
        fireworkMade = True
        
    if palmFirework >= 3 and willowFirework >= 3 and crossetteFirework >= 3:
        enoughFirework = True
        break

    if not fireworkMade:
        valueToBeMoved = effects[0] - 1
        effects.pop(0)
        effects.append(valueToBeMoved)
        

if enoughFirework:
    print (f"Congrats! You made the perfect firework show!")
else:
    print (f"Sorry. You can't make the perfect firework show.")

if effects:
    print (f"Firework Effects left: {', '.join(map(str, effects))}")
if power:
    print (f"Explosive Power left: {', '.join(map(str, power))}")

print (f"Palm Fireworks: {palmFirework}\nWillow Fireworks: {willowFirework}\nCrossette Fireworks: {crossetteFirework}")
