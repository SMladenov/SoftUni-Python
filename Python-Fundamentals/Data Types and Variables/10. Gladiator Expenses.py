#Gladiator Expenses

lostFights = int(input())
helmetPrice = float(input())
swordPrice = float(input())
shieldPrice = float(input())
armorPrice = float(input())

totalCost = 0
shieldBrakeCount = 0

for i in range(1, lostFights + 1):
    
    if i % 2 == 0:
        totalCost += helmetPrice
    if i % 3 == 0:
        totalCost += swordPrice
        if i % 2 == 0:
            totalCost += shieldPrice
            shieldBrakeCount += 1
            if shieldBrakeCount == 2:
                totalCost += armorPrice
                shieldBrakeCount = 0

print (f"Gladiator expenses: {totalCost:.2f} aureus")
