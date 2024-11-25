#Cooking Masterclass

import math

budget = float(input())
students = int(input())
priceFlour = float(input())
priceEgg = float(input())
priceApron = float(input())

freePackages = 0

if students >= 5:
    tempStudents = students
    while tempStudents > 0:
        tempStudents -= 5
        freePackages += 1

allMoneyNeeded = priceApron * math.ceil(students * 1.2) + ((priceEgg * 10) * students) + (priceFlour * (students - freePackages))

if allMoneyNeeded <= budget:
    print (f"Items purchased for {allMoneyNeeded:.2f}$.")
else:
    print (f"{(allMoneyNeeded - budget):.2f}$ more needed.")