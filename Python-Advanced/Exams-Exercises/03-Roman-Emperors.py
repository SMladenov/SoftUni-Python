#Roman Emperors

def list_roman_emperors(*args, **kwargs):

    dicSuccessful = {}
    dicUnSuccessful = {}
    
    for name, success in args:
        if success == True:
            dicSuccessful[name] = kwargs[name]
        else:
            dicUnSuccessful[name] = kwargs[name]

    listToOutput = []

    listToOutput.append(f"Total number of emperors: {len(args)}")
    
    if dicSuccessful:
        dicSuccessfulSorted = dict(sorted(dicSuccessful.items(), key= lambda x: (-x[1], x[0])))

        listToOutput.append(f"Successful emperors:")
        for name, years in dicSuccessfulSorted.items():
            listToOutput.append(f"****{name}: {years}")
        
    if dicUnSuccessful:
        dicUnsuccessfulSorted = dict(sorted(dicUnSuccessful.items(), key= lambda x: (x[1], x[0])))

        listToOutput.append(f"Unsuccessful emperors:")
        for name, years in dicUnsuccessfulSorted.items():
            listToOutput.append(f"****{name}: {years}")
    
    return '\n'.join(listToOutput)


#print(list_roman_emperors(("Augustus", True), ("Nero", False), Augustus=40, Nero=14,))

print(list_roman_emperors(("Augustus", True), ("Trajan", True), ("Nero", False), ("Caligula", False), ("Pertinax", False), ("Vespasian", True), Augustus=40, Trajan=19, Nero=14, Caligula=4, Pertinax=4, Vespasian=19,))

#print(list_roman_emperors(("Augustus", True), ("Trajan", True), ("Claudius", True), Augustus=40, Trajan=19, Claudius=13,))
