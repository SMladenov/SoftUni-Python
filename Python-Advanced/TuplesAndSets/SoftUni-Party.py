#SoftUni Party

import re

def isLen(someString):
    if len(someString) == 8:
        return True
    else:
        return False

numbersOfGuests = int(input())
setNormal = set()
setVIP = set()

for _ in range (numbersOfGuests):
    reservationCode = input().strip()
    if isLen(reservationCode):
        if re.match(r"^[0-9]{1,}", reservationCode):
            setVIP.add(reservationCode)
        else:
            setNormal.add(reservationCode)

peopleAttended = input().strip()

while peopleAttended != "END":
    if isLen(peopleAttended):
        if re.match(r"^[0-9]{1,}", peopleAttended):
            setVIP.discard(peopleAttended)
        else:
            setNormal.discard(peopleAttended)
        peopleAttended = input().strip()

sortedVIP = sorted(setVIP, reverse=False)
sortedNormal = sorted(setNormal, reverse=False)

print (f"{len(setVIP) + len(setNormal)}")
if sortedVIP:
    print ('\n'.join(sortedVIP))
if sortedNormal:
    print ('\n'.join(sortedNormal))