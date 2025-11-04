#A Miner Task

resource = input()

dictResources = {}

while resource != "stop":
    quantity = int(input())
    if resource not in dictResources.keys():
        dictResources[resource] = quantity
    else:
        dictResources[resource] += quantity
    resource = input()

for key, value in dictResources.items():
    print (f"{key} -> {value}")