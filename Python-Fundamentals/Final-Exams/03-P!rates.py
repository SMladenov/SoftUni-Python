#P!rates

cmd1 = input()

dicCities = {}

while cmd1 != "Sail":
    cmdSplit = cmd1.split('||')
    city = cmdSplit[0]
    population = int(cmdSplit[1])
    gold = int(cmdSplit[2])
    if city not in dicCities.keys():
        dicCities[city] = {'population': population, 'gold': gold}
    else:
        dicCities[city]['population'] += population
        dicCities[city]['gold'] += gold
    cmd1 = input()

events = input()

while events != "End":
    eventsSplit = events.split('=>')
    action = eventsSplit[0]
    town = eventsSplit[1]
    if action == "Plunder":
        people = int(eventsSplit[2])
        gold = int(eventsSplit[3])
        print (f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        dicCities[town]['population'] -= people
        dicCities[town]['gold'] -= gold
        if dicCities[town]['population'] <= 0 or dicCities[town]['gold'] <= 0:
            print (f"{town} has been wiped off the map!")
            dicCities.pop(town)
    if action == "Prosper":
        gold = int(eventsSplit[2])
        if gold >= 0:
            dicCities[town]['gold'] += gold
            print (f"{gold} gold added to the city treasury. {town} now has {dicCities[town]['gold']} gold.")
        else:
            print (f"Gold added cannot be a negative number!")
    events = input()


if len(dicCities) > 0:
    print (f"Ahoy, Captain! There are {len(dicCities)} wealthy settlements to go to:")
    for key, value in dicCities.items():
        print (f"{key} -> Population: {value['population']} citizens, Gold: {value['gold']} kg")
else:
    print (f"Ahoy, Captain! All targets have been plundered and destroyed!")
    