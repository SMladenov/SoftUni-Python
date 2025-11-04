#Quest in the Woods

days = int(input())
participants = int(input())
groupEnergy = float(input())
waterDayOnePerson = float(input())
foodDayOnePerson = float(input())

totalWater = days * participants * waterDayOnePerson
totalFood = days * participants * foodDayOnePerson

outOfEnergy = False

for i in range (1, days + 1):
    energyNeeded = float(input())
    if i % 2 == 0:
        totalWater *= 0.7
    if i % 3 == 0:
        totalFood -= (totalFood / participants)
    if (groupEnergy - energyNeeded) > 0:
        groupEnergy -= energyNeeded
    if (groupEnergy - energyNeeded) <= 0:
        print (f"You will run out of energy. You will be left with {totalFood:.2f} food and {totalWater:.2f} water.")
        outOfEnergy = True
        break
    if i % 2 == 0:
        groupEnergy *= 1.05
    if i % 3 == 0:
        groupEnergy *= 1.10
        
if not outOfEnergy:
    print (f"You are ready for the quest. You will be left with {groupEnergy:.2f} energy!")