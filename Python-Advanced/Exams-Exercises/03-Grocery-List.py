#Grocery List

def shop_from_grocery_list (*args):

    budget = args[0]
    productsNeeded = list(args[1])
    tupleProducts = args[2:]

    for product, price in tupleProducts:
        if product in productsNeeded and (budget - price) >= 0:
            budget -= price
            productsNeeded.remove(product)
        elif budget < price:
            break

    if not productsNeeded:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        return f"You did not buy all the products. Missing products: {', '.join(productsNeeded)}."

# print(shop_from_grocery_list(
#     100,
#     ["tomato", "cola"],
#     ("cola", 5.8),
#     ("tomato", 10.0),
#     ("tomato", 20.45),
# ))

# print(shop_from_grocery_list(
#     100,
#     ["tomato", "cola", "chips", "meat"],
#     ("cola", 5.8),
#     ("tomato", 10.0),
#     ("meat", 22),
# ))

print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))
