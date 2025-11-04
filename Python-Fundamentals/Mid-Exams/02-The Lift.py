#The Lift

people = int(input())
lift = [int(i) for i in input().split(' ')]

areBoarded = False

for index, i in enumerate(lift):
        
    if i < 4:
        if (people - 4) >= 0:
            difference = 4 - i
            lift[index] += difference
            people -= difference
        elif (people - 4) < 0:
            freeSlots = 4 - i
            if freeSlots >= people:
                lift[index] += people
                people -= people
            elif freeSlots < people:
                #difference = people - freeSlots
                lift[index] += freeSlots
                people -= freeSlots
    
    if people <= 0:
        areBoarded = True
        break

if not areBoarded:
    toString = [str(i) for i in lift]
    print (f"There isn't enough space! {people} people in a queue!\n{' '.join(toString)}")
else:
    toString = [str(i) for i in lift]
    leftLift = [i for i in lift if i != 4]
    if leftLift:
        print (f"The lift has empty spots!\n{' '.join(toString)}")
    else:
        print (f"{' '.join(toString)}")
