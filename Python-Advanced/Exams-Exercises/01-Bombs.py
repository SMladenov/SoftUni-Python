#Bombs

effects = [int(i) for i in input().split(', ')]
casings = [int(i) for i in input().split(', ')]

def getMaterial (amount):
    dicMaterials = {amount == 40: "Datura Bombs", amount == 60: "Cherry Bombs", amount == 120: "Smoke Decoy Bombs"}
    return dicMaterials.get(True, None)


dicBombs = {"Cherry Bombs": 0, "Datura Bombs": 0, "Smoke Decoy Bombs": 0}
enoughBombs = False

while effects and casings:
    currentEffect = effects[0]
    currentCasing = casings[-1]

    sumBoth = currentEffect + currentCasing
    resultMaterial = getMaterial(sumBoth)

    if resultMaterial is not None:
        dicBombs[resultMaterial] += 1
        effects.pop(0)
        casings.pop()
        if dicBombs["Cherry Bombs"] >= 3 and dicBombs["Datura Bombs"] >= 3 and dicBombs["Smoke Decoy Bombs"] >= 3:
            enoughBombs = True
            break

    elif resultMaterial is None:
        casings[-1] -= 5


if enoughBombs:
    print (f"Bene! You have successfully filled the bomb pouch!")
else:
    print (f"You don't have enough materials to fill the bomb pouch.")

if effects:
    print (f"Bomb Effects: {', '.join(map(str, effects))}")
else:
    print (f"Bomb Effects: empty")

if casings:
    print (f"Bomb Casings: {', '.join(map(str, casings))}")
else:
    print (f"Bomb Casings: empty")

for bomb, value in dicBombs.items():
    print (f"{bomb}: {value}")
