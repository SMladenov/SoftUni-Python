#Destination Mapper

import re

destinations = input()

patternDestinations = r"(?<=([\/=]))([A-Z][a-zA-Z]{2,})(?=\1)"

destMatches = re.findall(patternDestinations, destinations)

totalPoints = 0
listDest = []

for i in destMatches:
    totalPoints += len(i[1])
    listDest.append(i[1])

print (f"Destinations: {', '.join(listDest)}\nTravel Points: {totalPoints}")