#Boarding Passengers

def boarding_passengers(*args):
    
    shipCapacity = int(args[0])
    passengers = args[1:]
    
    dicBoarded = {}
    boardedGroups = 0

    for number, group in passengers:
        if shipCapacity - number >= 0:
            if group not in dicBoarded.keys():
                dicBoarded[group] = number
            else:
                dicBoarded[group] += number
            shipCapacity -= number
            boardedGroups += 1
            if shipCapacity == 0:
                break

    dicBoardedSorted = dict(sorted(dicBoarded.items(), key=lambda x: (-x[1], x[0])))

    listForOutput = []

    listForOutput.append(f"Boarding details by benefit plan:")
    for group, people in dicBoardedSorted.items():
        listForOutput.append(f"## {group}: {people} guests")

    if boardedGroups == len(passengers) and shipCapacity == 0:
        listForOutput.append(f"All passengers are successfully boarded!")
    elif boardedGroups < len(passengers) and shipCapacity == 0:
        listForOutput.append(f"Boarding unsuccessful. Cruise ship at full capacity.")
    elif boardedGroups < len(passengers) and shipCapacity > 0:
        listForOutput.append(f"Partial boarding completed. Available capacity: {shipCapacity}.")

    return '\n'.join(listForOutput)

#print(boarding_passengers(150, (35, 'Diamond'), (55, 'Platinum'), (35, 'Gold'), (25, 'First Cruiser')))

#print(boarding_passengers(100, (20, 'Diamond'), (15, 'Platinum'), (25, 'Gold'), (25, 'First Cruiser'), (15, 'Diamond'), (10, 'Gold')))

print(boarding_passengers(120, (30, 'Gold'), (20, 'Platinum'), (30, 'Diamond'), (10, 'First Cruiser'), (31, 'Platinum'), (20, 'Diamond')))
