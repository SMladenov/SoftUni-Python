#Water Dispenser

waterQuantity = int(input())
queuePeople = []

human = input()

while human != "Start":
    queuePeople.append(human)
    human = input()

cmd = input()

while cmd != "End":
    cmdSplit = cmd.split(' ')
    if len(cmdSplit) == 1:
        quantity = int(cmdSplit[0])
        if waterQuantity - quantity >= 0:
            print (f"{queuePeople.pop(0)} got water")
            waterQuantity -= quantity
        else:
            print (f"{queuePeople.pop(0)} must wait")
    else:
        refillQuantity = int(cmdSplit[1])
        waterQuantity += refillQuantity
    cmd = input()

print (f"{waterQuantity} liters left")