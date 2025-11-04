#Energy Drinks

caffeine = [int(i) for i in input().split(', ')]
drinks = [int(i) for i in input().split(', ')]

totalCaffeine = 0

while caffeine and drinks:
    currentCaffeine = caffeine[-1]
    amountDrinks = drinks[0]
    sumCaff = currentCaffeine * amountDrinks

    if totalCaffeine + sumCaff <= 300:
        caffeine.pop()
        drinks.pop(0)
        totalCaffeine += sumCaff

    else:
        caffeine.pop()
        drinks.pop(0)
        drinks.append(amountDrinks)
        if totalCaffeine > 0:
            totalCaffeine -= 30
            if totalCaffeine < 0:
                totalCaffeine = 0

if drinks:
    print (f"Drinks left: {', '.join(map(str, drinks))}")
else:
    print (f"At least Stamat wasn't exceeding the maximum caffeine.")

print (f"Stamat is going to sleep with {totalCaffeine} mg caffeine.")
