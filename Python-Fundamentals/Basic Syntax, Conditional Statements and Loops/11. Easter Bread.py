#Easter Bread

budget = float(input())
pricekgFlour = float(input())
pricePackEggs = pricekgFlour * 0.75
priceLiterMilk = pricekgFlour * 1.25

costLoaf = pricekgFlour + pricePackEggs + (priceLiterMilk * 0.25)

counterLoaves = 0
coloredEggs = 0

while budget > 0:
    if (budget - costLoaf) >= 0:
        counterLoaves += 1
        coloredEggs += 3
        budget -= costLoaf
        if counterLoaves % 3 == 0:
            coloredEggs -= (counterLoaves - 2)
    else:
        break

print (f"You made {counterLoaves} loaves of Easter bread! Now you have {coloredEggs} eggs and {budget:.2f}BGN left.")
