#Furniture

import re

quantity = r"(?<=!)\d+"
furniture = r"(?<=>>)[a-zA-Z]+(?=<<)"
price = "(?<=<<)(?:[1-9]\d*|0)(?:\.\d+)?(?=!)"
#price = r"(?<=<<)\d+\.?\d*(?=!)"
#price = r"(?<=<<)[\d.]+(?=!)"

def getPurchase(cmd):
    listQuantity = re.findall(quantity, cmd)
    listFurniture = re.findall(furniture, cmd)
    listPrice = re.findall(price, cmd)

    # If any of the lists are empty, return "invalid"
    if not listQuantity or not listFurniture or not listPrice:
        return "invalid"
    else:
        # Return the first match found in each category
        return [listQuantity[0], listPrice[0], listFurniture[0]]

# Main logic
cmd = input()
totalAmount = 0
listValidFurnitures = []

while cmd != "Purchase":
    result = getPurchase(cmd)
    if result != "invalid":
        # Calculate the total cost
        totalAmount += (int(result[0]) * float(result[1]))
        listValidFurnitures.append(result[2])
    cmd = input()

# Print the results
print(f"Bought furniture:")
for furniture in listValidFurnitures:
    print(furniture)
print(f"Total money spend: {totalAmount:.2f}")