#Truck Tour

petrolPumps = int(input())

queuePetrol = []
queueDistance = []

for i in range (0, petrolPumps):
    pumpInfo = input().strip().split(' ')
    queuePetrol.append(int(pumpInfo[0]))
    queueDistance.append(int(pumpInfo[1]))

pumpIndex = 0
isEnough = False

while pumpIndex < len(queuePetrol):
    currentTank = 0
    currentDistance = 0
    amountPetrol = queuePetrol[pumpIndex]
    distanceKm = queueDistance[pumpIndex]
    if amountPetrol >= distanceKm:
        tempqPetrol = queuePetrol[pumpIndex:len(queuePetrol)] + queuePetrol[0:pumpIndex]
        tempqDistance = queueDistance[pumpIndex:len(queueDistance)] + queueDistance[0:pumpIndex]
        for i in range (0, len(tempqPetrol)):
            currentTank += tempqPetrol[i]
            currentTank -= tempqDistance[i]
            if currentTank < 0:
                break
        if currentTank >= 0:
            isEnough = True
            break
            
    pumpIndex += 1

if isEnough:
    print (f"{pumpIndex}")
 