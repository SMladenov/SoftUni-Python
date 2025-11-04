#Apocalypse Preparation

textiles = [int(i) for i in input().split()]
medicaments = [int(i) for i in input().split()]

dicCreatedItems = {}

def getHeal (amount):
    dicHealingItems = {amount == 30: "Patch",
                      amount == 40: "Bandage",
                      amount == 100: "MedKit"}
    return dicHealingItems.get(True, None)


while textiles and medicaments:
    currentTextile = textiles[0]
    currentMedica = medicaments[-1]
    sumBoth = currentTextile + currentMedica

    getItem = getHeal(sumBoth)
    
    if getItem is not None:
        if getItem not in dicCreatedItems.keys():
            dicCreatedItems[getItem] = 1
        else:
            dicCreatedItems[getItem] += 1
        textiles.pop(0)
        medicaments.pop()

    elif sumBoth > 100:
        if 'MedKit' in dicCreatedItems.keys():
            dicCreatedItems['MedKit'] += 1
        else:
            dicCreatedItems['MedKit'] = 1
        textiles.pop(0)
        medicaments.pop()
        if len(medicaments) > 0:
            medicaments[-1] += sumBoth - 100
        else:
            medicaments.append(sumBoth - 100)

    else:
        textiles.pop(0)
        medicaments[-1] += 10
        
if not textiles and not medicaments:
    print (f"Textiles and medicaments are both empty.")
if textiles and not medicaments:
    print (f"Medicaments are empty.")
if medicaments and not textiles:
    print (f"Textiles are empty.")

if dicCreatedItems:
    dicCreatedItemsSorted = dict(sorted(dicCreatedItems.items(), key=lambda x: (-x[1], x[0])))
    for name, amount in dicCreatedItemsSorted.items():
        print (f"{name} - {amount}")

if medicaments:
    medicaments.reverse()
    print (f"Medicaments left: {', '.join(map(str, medicaments))}")
if textiles:
    print (f"Textiles left: {', '.join(map(str, textiles))}")
