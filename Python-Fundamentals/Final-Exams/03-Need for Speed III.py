#Need for Speed III

numberOfCars = int(input())

dicCars = {}

for i in range (numberOfCars):
    cmdSplit = input().split('|')
    car = cmdSplit[0]
    mileage = int(cmdSplit[1])
    fuel = int(cmdSplit[2])
    if car not in dicCars.keys():
        dicCars[car] = {'mileage': mileage, 'fuel': fuel}

cmd = input()

while cmd != "Stop":
    cmdSplit = cmd.split(':')
    cmdSplit = [i.strip() for i in cmdSplit if i.strip()]
    action = cmdSplit[0]
    car = cmdSplit[1]
    
    #Action 1
    if action == "Drive":
        distance = int(cmdSplit[2])
        fuel = int(cmdSplit[3])
        if (dicCars[car]['fuel'] - fuel >= 0):
            if (dicCars[car]['mileage'] + distance) < 100000:
                dicCars[car]['fuel'] = dicCars[car]['fuel'] - fuel
                dicCars[car]['mileage'] = dicCars[car]['mileage'] + distance
                print (f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
                
            elif (dicCars[car]['mileage'] + distance) >= 100000:
                print (f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
                print (f"Time to sell the {car}!")
                dicCars.pop(car)
        else:
            print (f"Not enough fuel to make that ride")

    #Action 2
    if action == "Refuel":
        fuel = int(cmdSplit[2])
        fuelNeeded = 75 - dicCars[car]['fuel']
        if fuel >= fuelNeeded:
            dicCars[car]['fuel'] = 75
            print (f"{car} refueled with {fuelNeeded} liters")
        else:
            dicCars[car]['fuel'] = dicCars[car]['fuel'] + fuel
            print (f"{car} refueled with {fuel} liters")

    #Action 3
    if action == "Revert":
        kilometers = int(cmdSplit[2])
        if (dicCars[car]['mileage'] - kilometers) >= 10000:
            print (f"{car} mileage decreased by {kilometers} kilometers")
            dicCars[car]['mileage'] = dicCars[car]['mileage'] - kilometers
        else:
            dicCars[car]['mileage'] = 10000
    
    cmd = input()

for key, value in dicCars.items():
    print (f"{key} -> Mileage: {value['mileage']} kms, Fuel in the tank: {value['fuel']} lt.")