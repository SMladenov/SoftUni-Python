#Snowballs

numberSnowballs = int(input())

finalWeight = 0
finalTime = 0
finalQuality = 0
finalValue = 0

for i in range (numberSnowballs):
    weight = int(input())
    time = int(input())
    quality = int(input())

    snowballValue = (weight // time) ** quality

    if snowballValue > finalValue:
        finalWeight = weight
        finalTime = time
        finalQuality = quality
        finalValue = snowballValue

print (f"{finalWeight} : {finalTime} = {finalValue} ({finalQuality})")
