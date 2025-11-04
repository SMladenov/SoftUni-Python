#Aladdin's Gifts

materials = [int(i) for i in input().split()]
magicLevels = [int(i) for i in input().split()]

dicPresents = {}

def getGift (magic):
    dicGifts = {100 <= magic <= 199: 'Gemstone', 
                200 <= magic <= 299: 'Porcelain Sculpture', 
                300 <= magic <= 399: 'Gold', 
                400 <= magic <= 499: 'Diamond Jewellery'}
    
    return dicGifts.get(True, None)

while materials and magicLevels:
    currentMaterial = materials[-1]
    currentLevel = magicLevels[0]

    sumMagic = currentMaterial + currentLevel

    gift = getGift(sumMagic)
    
    if gift is None:
        if sumMagic < 100:
            if sumMagic % 2 == 0:
                currentMaterial *= 2
                currentLevel *= 3
                sumMagic = currentMaterial + currentLevel
                gift = getGift(sumMagic)
                if gift is None:
                    materials.pop()
                    magicLevels.pop(0)
            elif sumMagic % 2 == 1:
                currentMaterial *= 2
                currentLevel *= 2
                sumMagic = currentMaterial + currentLevel
                gift = getGift(sumMagic)
                if gift is None:
                    materials.pop()
                    magicLevels.pop(0)

        elif sumMagic > 499:
            sumMagic //= 2
            gift = getGift(sumMagic)
            if gift is None:
                materials.pop()
                magicLevels.pop(0)
            
    if gift:
        if gift not in dicPresents.keys():
            dicPresents[gift] = 1
        else:
            dicPresents[gift] += 1
        materials.pop()
        magicLevels.pop(0)

if ('Gemstone' in dicPresents.keys() and 'Porcelain Sculpture' in dicPresents.keys()) \
or ('Gold' in dicPresents.keys() and 'Diamond Jewellery' in dicPresents.keys()):
    print (f"The wedding presents are made!")
else:
    print (f"Aladdin does not have enough wedding presents.")

if materials:
    print (f"Materials left: {', '.join(map(str, materials))}")
if magicLevels:
    print (f"Magic left: {', '.join(map(str, magicLevels))}")

if dicPresents:
    dicPresentsSorted = dict(sorted(dicPresents.items(), key= lambda x: x[0]))

    for present, value in dicPresentsSorted.items():
        print (f"{present}: {value}")
