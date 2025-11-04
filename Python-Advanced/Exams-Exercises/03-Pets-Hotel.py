#Pets Hotel

def accommodate_new_pets(*args):

    accomodatedPets = {}
    
    hotelCapacity = int(args[0])
    weightLimit = float(args[1])
    pets = list(args[2:])

    while pets:
        if hotelCapacity > 0:
            typePet, weight = pets.pop(0)
            if weight <= weightLimit:
                if typePet not in accomodatedPets.keys():
                    accomodatedPets[typePet] = 1
                else:
                    accomodatedPets[typePet] += 1
                hotelCapacity -= 1
        else:
            break

    sortedPets = dict(sorted(accomodatedPets.items(), key=lambda x: x[0]))
    listToPrint = []
    for key, value in sortedPets.items():
        formattedString = f"{key}: {value}"
        listToPrint.append(formattedString)

    if not pets:
        return f"All pets are accommodated! Available capacity: {hotelCapacity}.\nAccommodated pets:\n" + "\n".join(listToPrint)
    else:
        return f"You did not manage to accommodate all pets!\nAccommodated pets:\n" + "\n".join(listToPrint)
    
print(accommodate_new_pets(
    10,
    15.0,
    ("cat", 5.8),
    ("dog", 10.0),
))

print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))

print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))
