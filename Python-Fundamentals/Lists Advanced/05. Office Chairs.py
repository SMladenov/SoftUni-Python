#Office Chairs

rooms = int(input())

chairsLeft = 0
chairsNeeded = False

for room in range (1, rooms + 1):
    strInput = input().split(' ')
    chairs = len(strInput[0])
    visitors = int(strInput[1])
    if chairs < visitors:
        print (f"{visitors - chairs} more chairs needed in room {room}")
        chairsNeeded = True
    else:
        chairsLeft += (chairs - visitors)
        
if not chairsNeeded:
    print (f"Game On, {chairsLeft} free chairs left")
    