#Orders

product = input()

drinks = {}

while product != "buy":
    productSplit = product.split(' ')
    drink = productSplit[0]
    price = float(productSplit[1])
    quantity = float(productSplit[2])
    if drink not in drinks.keys():
        drinks[drink] = []
        drinks[drink].append(price)
        drinks[drink].append(quantity)
    else:
        drinks[drink][1] += quantity 
        tempPrice = drinks[drink][0]
        if tempPrice != price:
            drinks[drink][0] = price
    product = input()

for key, value in drinks.items():
    print (f"{key} -> {(value[0] * value[1]):.2f}")