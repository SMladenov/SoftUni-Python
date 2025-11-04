#Chicken Snack

money = [int(i) for i in input().split()]
prices = [int(i) for i in input().split()]

foodCount = 0

while money and prices:
    currentMoney = money[-1]
    currentPrice = prices[0]
    if currentMoney == currentPrice:
        money.pop(-1)
        prices.pop(0)
        foodCount += 1
        
    elif currentMoney > currentPrice:
        change = currentMoney - currentPrice
        money.pop(-1)
        prices.pop(0)
        foodCount += 1
        if not money:
            money.append(change)
        elif money:
            money[-1] += change
        

    elif currentMoney < currentPrice:
        money.pop(-1)
        prices.pop(0)

if foodCount >= 4:
    print (f"Gluttony of the day! Henry ate {foodCount} foods.")
elif 0 < foodCount < 4:
    if foodCount == 1:
        print (f"Henry ate: {foodCount} food.")
    else:
        print (f"Henry ate: {foodCount} foods.")
else:
    print (f"Henry remained hungry. He will try next weekend again.")
