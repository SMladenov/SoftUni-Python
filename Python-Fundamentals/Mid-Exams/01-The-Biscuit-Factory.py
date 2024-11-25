#The Biscuit Factory

import math

biscuitsPerDay = int(input())
workers = int(input())
biscuitsCompetition = int(input())

ourProduction = 0

for i in range (1, 31):
    if i % 3 == 0:
        production = math.floor((biscuitsPerDay * workers) * 0.75)
        ourProduction += production
    else:
        ourProduction += (biscuitsPerDay * workers)

print (f"You have produced {ourProduction} biscuits for the past month.")
if ourProduction > biscuitsCompetition:
    difference = ourProduction - biscuitsCompetition
    percentage = (difference / biscuitsCompetition) * 100
    print (f"You produce {percentage:.2f} percent more biscuits.")
else:
    difference = biscuitsCompetition - ourProduction
    percentage = (difference / biscuitsCompetition) * 100
    print (f"You produce {percentage:.2f} percent less biscuits.")