#SoftUni Parking

numberCommands = int(input())

dicCars = {}

for i in range (numberCommands):
    cmd = input().split(' ')
    action = cmd[0]
    name = cmd[1]
    if action == "register":
        plate = cmd[2]
        if name not in dicCars.keys():
            dicCars[name] = plate
            print (f"{name} registered {plate} successfully")
        else:
            print (f"ERROR: already registered with plate number {plate}")
    if action == "unregister":
        if name not in dicCars.keys():
            print (f"ERROR: user {name} not found")
        else:
            dicCars.pop(name)
            print (f"{name} unregistered successfully")

for key, value in dicCars.items():
    print (f"{key} => {value}")