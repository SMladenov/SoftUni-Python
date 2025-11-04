#Shopping Cart

def shopping_cart (*args):

    dicMeals = {"Soup": [], "Pizza": [], "Dessert": []}

    hasProducts = False
    
    for el in args:
        if isinstance(el, str) and el == "Stop":
            break
        else:
            meal, product = el
            if meal == "Soup":
                if len(dicMeals[meal]) < 3 and product not in dicMeals[meal]:
                    dicMeals[meal].append(product)
                    hasProducts = True
            elif meal == "Pizza":
                if len(dicMeals[meal]) < 4 and product not in dicMeals[meal]:
                    dicMeals[meal].append(product)
                    hasProducts = True
            elif meal == "Dessert":
                if len(dicMeals[meal]) < 2 and product not in dicMeals[meal]:
                    dicMeals[meal].append(product)
                    hasProducts = True

    if not hasProducts:
        return f"No products in the cart!"
    
    dicMealsSorted = dict(sorted(dicMeals.items(), key= lambda x: (-len(x[1]), x[0])))

    listToOutput = []

    for meal, products in dicMealsSorted.items():
        products.sort()
        listToOutput.append(f"{meal}:")
        for product in products:
            listToOutput.append(f" - {product}")

    return '\n'.join(listToOutput)

print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))

# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'ham'),
#     'Stop',
# ))

# print(shopping_cart(
#     'Stop',
#     ('Pizza', 'ham'),
#     ('Pizza', 'mushrooms'),
# ))

    