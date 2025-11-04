#Man O War

pirateShip = [int(i) for i in input().split('>')]
warShip = [int(i) for i in input().split('>')]
maxHealthSection = int(input())

cmd = input()
pirateWon = False
warWon = False

while cmd != "Retire":
    cmdSplit = cmd.split(' ')
    action = cmdSplit[0]

    #The Pirate Ship attacks the War Ship
    if action == "Fire":
        index = int(cmdSplit[1])
        damage = int(cmdSplit[2])
        if 0 <= index < len(warShip):
            health = warShip[index]
            if (health - damage) <= 0:
                print (f"You won! The enemy ship has sunken.")
                pirateWon = True
                break
            else:
                warShip[index] -= damage
    
    #The War Ship attacks the Pirate Ship
    if action == "Defend":
        startIndex = int(cmdSplit[1])
        endIndex = int(cmdSplit[2])
        damage = int(cmdSplit[3])
        if 0 <= startIndex < len(pirateShip) and 0 <= endIndex < len(pirateShip):
            if startIndex <= endIndex:
                for i in range (startIndex, endIndex + 1):
                    health = pirateShip[i]
                    if (health - damage) <= 0:
                        print (f"You lost! The pirate ship has sunken.")
                        warWon = True
                        break
                    else:
                        pirateShip[i] -= damage
                if warWon:
                    break
        
    #The Crew Repairs a section of the Pirate Ship
    if action == "Repair":
        index = int(cmdSplit[1])
        health = int(cmdSplit[2])
        if 0 <= index < len(pirateShip):
            currentSectionHealth = pirateShip[index]
            if (health + currentSectionHealth) > maxHealthSection:
                pirateShip[index] = maxHealthSection
            else:
                pirateShip[index] += health

    #Prints the count of all section of the Pirate Ship that need repair
    if action == "Status":
        sectionsForRepair = [i for i in pirateShip if i < (maxHealthSection * 0.2)]
        print (f"{len(sectionsForRepair)} sections need repair.")

    cmd = input()

if not pirateWon and not warWon:
    print (f"Pirate ship status: {sum(pirateShip)}\nWarship status: {sum(warShip)}")