#Treasure Hunt

chest = input().split('|')
cmd = input()

while cmd != "Yohoho!":
    cmdSplit = cmd.split(' ')
    action = cmdSplit[0]
    listStolenItems = []

    if action == "Loot":
        listToInsert = [cmdSplit[i] for i in range (1, len(cmdSplit))]
        for i in listToInsert:
            if i not in chest:
                chest.insert(0, i)
                
    if action == "Drop":
        index = int(cmdSplit[1])
        if 0 <= index <= (len(chest) - 1):
            loot = chest.pop(index)
            chest.append(loot)
            
    if action == "Steal":
        count = int(cmdSplit[1])
        if count < len(chest):
            indexUntil = (len(chest) - 1) - count
            for i in range (len(chest) - 1, indexUntil, -1):
                loot = chest[i]
                listStolenItems.insert(0, loot)
                chest.pop(len(chest) - 1)
            print (f"{', '.join(listStolenItems)}")
        else:
            listStolenItems = chest
            print (f"{', '.join(listStolenItems)}")
            chest.clear()
    cmd = input()

if not chest:
    print (f"Failed treasure hunt.")
else:
    averageGain = 0
    for i in chest:
        averageGain += len(i)
    averageGain /= len(chest)
    print (f"Average treasure gain: {averageGain:.2f} pirate credits.")