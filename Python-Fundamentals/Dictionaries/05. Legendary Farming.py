#Legendary Farming

import sys

# Read all input at once
input_data = sys.stdin.read().strip()
lines = input_data.splitlines()

materials = []

for line in lines:
    materials.extend(line.split())

dictMaterials = {}
listLegendary = ["shards", "fragments", "motes"]

for i in range (0, len(materials), + 2):
    quantity = int(materials[i])
    material = materials[i + 1].lower()
    if material in dictMaterials.keys():
        dictMaterials[material] += quantity
    if material not in dictMaterials.keys():
        dictMaterials[material] = quantity
    if material in listLegendary and (dictMaterials[material] >= 250):
        dictMaterials[material] -= 250
        if material == 'shards':
            print (f"Shadowmourne obtained!")
            break
        if material == 'fragments':
            print (f"Valanyr obtained!")
            break
        if material == 'motes':
            print (f"Dragonwrath obtained!")
            break

#sortedDict = dict(sorted(dictMaterials.items(), key=lambda i:  i[0], reverse=True))

dictImportantItems = {"shards": 0, "fragments": 0, "motes": 0}
for key, value in dictMaterials.items():
    if key in listLegendary:
        dictImportantItems[key] += value
        #dictMaterials.pop(key)

for key, value in dictImportantItems.items():
    print (f"{key}: {value}")

for key, value in dictMaterials.items():
    if key not in listLegendary:
        print (f"{key}: {value}")