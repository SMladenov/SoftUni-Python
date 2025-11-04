#Planting Garden System

def plant_garden(*args, **kwargs):
    
    availableSpace = float(args[0])

    allowedTypes = {plant: space for plant, space in args[1:]}

    sortedRequests = dict(sorted(kwargs.items(), key= lambda x: x[0]))

    dicPlanted = {}

    fullyPlanted = True
    
    for plant, quantity in sortedRequests.items():
        if plant in allowedTypes.keys():
            totalValue = allowedTypes[plant] * quantity
            
            if totalValue <= availableSpace:
                availableSpace -= totalValue
                dicPlanted[plant] = quantity
            else:
                availableQuantity = int(availableSpace // allowedTypes[plant])
                availableSpace -= availableQuantity * allowedTypes[plant]
                if availableQuantity > 0:
                    dicPlanted[plant] = availableQuantity
                    
                fullyPlanted = False

    listForOutput = []
    
    if fullyPlanted:
        listForOutput.append(f"All plants were planted! Available garden space: {availableSpace:.1f} sq meters.")
    else:
        listForOutput.append(f"Not enough space to plant all requested plants!")

    sortedDicPlanted = dict(sorted(dicPlanted.items(), key= lambda x: x[0]))

    listForOutput.append(f"Planted plants:")
    for key, value in sortedDicPlanted.items():
        listForOutput.append(f"{key}: {value}")
        
    return '\n'.join(listForOutput)

#print(plant_garden(50.0, ("rose", 2.5), ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20))

#print(plant_garden(20.0, ("rose", 2.0), ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20, sunflower=5))

#print(plant_garden(2.0, ("rose", 2.5), ("tulip", 1.2), ("daisy", 0.2), rose=4, tulip=15, sunflower=3, daisy=4))

print(plant_garden(50.0, ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20, daisy=1))
