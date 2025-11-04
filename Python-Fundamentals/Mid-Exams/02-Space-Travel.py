#Space Travel

travel = input().split('||')
fuel = int(input())
ammunition = int(input())

for i in travel:
    if i == "Titan":
        print (f"You have reached Titan, all passengers are safe.")
    else:
        iSplit = i.split(' ')
        cmd = iSplit[0]

        #Case 1
        if cmd == "Travel":
            years = int(iSplit[1])
            if (fuel - years) >= 0:
                fuel -= years
                print (f"The spaceship travelled {years} light-years.")
            else:
                print (f"Mission failed.")
                break

        #Case 2
        if cmd == "Enemy":
            armor = int(iSplit[1])
            if (ammunition - armor) >= 0:
                ammunition -= armor
                print (f"An enemy with {armor} armour is defeated.")
            else:
                fuelNeededToRun = armor * 2
                if (fuel - fuelNeededToRun) >= 0:
                    fuel -= fuelNeededToRun
                    print (f"An enemy with {armor} armour is outmaneuvered.")
                else:
                    print (f"Mission failed.")
                    break

        #Case 3
        if cmd == "Repair":
            amount = int(iSplit[1])
            fuel += amount
            ammunition += (amount * 2)
            print (f"Ammunitions added: {amount * 2}.\nFuel added: {amount}.")