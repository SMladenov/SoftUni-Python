#Plan Discovery

inputNumber = int(input())

dicPlants = {}

for i in range (inputNumber):
    plantInput = input().split('<->')
    plant = plantInput[0]
    rarity = plantInput[1]
    if plant not in dicPlants.keys():
        dicPlants[plant] = {'rarity': rarity, 'rating': []}
    else:
        dicPlants[plant]['rarity'] = rarity


cmd = input()

while cmd != "Exhibition":
    actionSplit = cmd.split(':')
    action = actionSplit[0]
    data = actionSplit[1].split('-')
    data = [i.strip() for i in data if i.strip()]
    plant = data[0]
    
    if action == "Rate":
        rating = float(data[1])
        if plant in dicPlants:
            dicPlants[plant]['rating'].append(rating)
        else:
            print (f"error")
    if action == "Update":
        newRarity = int(data[1])
        if plant in dicPlants:
            dicPlants[plant]['rarity'] = newRarity
        else:
            print (f"error")
    if action == "Reset":
        if plant in dicPlants:
            dicPlants[plant]['rating'].clear()
        else:
            print (f"error")
    cmd = input()

print (f"Plants for the exhibition:")
for key, value in dicPlants.items():
    averageRating = 0
    if value['rating']:
        averageRating = sum(value['rating']) / len(value['rating'])
    print (f"- {key}; Rarity: {value['rarity']}; Rating: {averageRating:.2f}")
    