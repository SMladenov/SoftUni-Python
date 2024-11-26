#Electron Distribution

electrons = int(input())

listShells = []

counter = 1

while electrons > 0:
    maxElectrons = 2 * (counter ** 2)
    if (electrons - maxElectrons) >= 0:
        electrons -= maxElectrons
        counter += 1
        listShells.append(maxElectrons)
    if (electrons - maxElectrons) < 0 and electrons != 0:
        listShells.append(electrons)
        break

print (f"{listShells}")
