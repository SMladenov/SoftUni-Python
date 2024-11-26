#Seize the Fire

cells = input().split('#')
water = int(input())

totalEffort = 0
totalFire = 0
cellsPutDown = []

for i in cells:
    fireCell = i.split(' ')
    fireLevel = fireCell[0]
    fireValue = int(fireCell[2])
    if fireLevel == "High":
        if 81 <= fireValue <= 125:
            effort = (fireValue + (fireValue * 0.25))
            if (water - effort) >= 0:
                water -= effort
                cellsPutDown.append(fireValue)
                totalFire += fireValue
                totalEffort += (fireValue * 0.25)
    if fireLevel == "Medium":
        if 51 <= fireValue <= 80:
            effort = (fireValue + (fireValue * 0.25))
            if (water - effort) >= 0:
                water -= effort
                cellsPutDown.append(fireValue)
                totalFire += fireValue
                totalEffort += (fireValue * 0.25)
    if fireLevel == "Low":
        if 1 <= fireValue <= 50:
            effort = (fireValue + (fireValue * 0.25))
            if (water - effort) >= 0:
                water -= effort
                cellsPutDown.append(fireValue)
                totalFire += fireValue
                totalEffort += (fireValue * 0.25)

print (f"Cells:")
for i in cellsPutDown:
    print (f" - {i}")
print (f"Effort: {totalEffort:.2f}\nTotal Fire: {totalFire}")