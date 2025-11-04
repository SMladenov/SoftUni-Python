#Offroad Challenge

fuelTank = [int(i) for i in input().split()]
additionalFuel = [int(i) for i in input().split()]
necessaryFuel = [int(i) for i in input().split()]

counter = 0
listAltitudes = []

while fuelTank and additionalFuel and necessaryFuel:
    actualFuel = fuelTank[-1] - additionalFuel[0]
    fuelNeeded = necessaryFuel[0]
    
    if actualFuel >= fuelNeeded:
        counter += 1
        listAltitudes.append(f"Altitude {counter}")
        fuelTank.pop()
        additionalFuel.pop(0)
        necessaryFuel.pop(0)
        print (f"John has reached: Altitude {counter}")
    else:
        print(f"John did not reach: Altitude {counter + 1}")
        break

if len(listAltitudes) == 4:
     print("John has reached all the altitudes and managed to reach the top!")
    
elif 0 < len(listAltitudes) < 4:
    print("John failed to reach the top.")
    print (f"Reached altitudes: {', '.join(listAltitudes)}")
elif not listAltitudes:
    print(f"John failed to reach the top.\nJohn didn't reach any altitude.")
