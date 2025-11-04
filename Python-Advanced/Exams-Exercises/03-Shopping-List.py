#Shopping List

def shopping_list (budget, **kwargs):

    listToOutput = []

    #productsBought = 0
    typesBought = []
    
    if budget >= 100:    
        for item, prices in kwargs.items():
            price, quantity = prices[0], prices[1]
            totalPrice = price * quantity
            if budget - totalPrice >= 0:
                budget -= totalPrice
                listToOutput.append(f"You bought {item} for {totalPrice:.2f} leva.")
                #productsBought += 1
                if item not in typesBought:
                    typesBought.append(item)
                    if len(typesBought) == 5:
                        break
    else:
        return f"You do not have enough budget."         

    return '\n'.join(listToOutput)

print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))

print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))

print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
