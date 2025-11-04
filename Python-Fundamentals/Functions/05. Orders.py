#Orders

def getPrice(product, quantity):
    dicPrices = {"coffee": 1.50, "water": 1.00, "coke": 1.40, "snacks": 2.00}
    price = dicPrices.get(product)
    return price * quantity

product = input()
quantity = int(input())

print (f"{getPrice(product, quantity):.2f}")
