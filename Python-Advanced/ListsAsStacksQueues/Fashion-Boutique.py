#Fashion Boutique
#Stack

clothes = [int(i) for i in input().strip().split(' ') if i.strip()]
rackCapacity = int(input())

racksUsed = 1
currentRack = rackCapacity

while clothes:
    currentClothe = clothes[len(clothes) - 1]
    if currentRack - currentClothe >= 0:
        currentRack -= currentClothe
        clothes.pop()
    else:
        racksUsed += 1
        currentRack = rackCapacity

print (f"{racksUsed}")
