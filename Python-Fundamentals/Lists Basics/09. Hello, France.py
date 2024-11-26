#Hello France

items = input().split('|')
budget = float(input())

itemsBought = 0
listBoughtItems = []
profit = 0


for i in items:
    iSplit = i.split('->')
    type = iSplit[0]
    price = float(iSplit[1])
    if type == "Clothes":
        if price <= 50.00:
            if (budget - price) >= 0:
                budget -= price
                sellPrice = price * 1.40
                itemsBought += sellPrice
                listBoughtItems.append(sellPrice)
                profit += (price * 0.4)
    if type == "Shoes":
        if price <= 35.00:
            if (budget - price) >= 0:
                budget -= price
                sellPrice = price * 1.40
                itemsBought += sellPrice
                listBoughtItems.append(sellPrice)
                profit += (price * 0.4)
    if type == "Accessories":
        if price <= 20.50:
            if (budget - price) >= 0:
                budget -= price
                sellPrice = price * 1.40
                itemsBought += sellPrice
                listBoughtItems.append(sellPrice)
                profit += (price * 0.4)


for i in listBoughtItems:
    print (f"{i:.2f}", end = ' ')

print (f"\nProfit: {profit:.2f}")

if (itemsBought + budget) >= 150:
    print (f"Hello, France!")
else:
    print (f"Not enough money.")


    