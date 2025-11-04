#Computer Store

price = input()
totalPrice = 0
totalTaxes = 0
priceWoTaxes = 0

while price != "regular" and price != "special":
    priceParse = float(price)
    if priceParse < 0:
        print (f"Invalid price!")
    else:
        priceWoTaxes += priceParse
        tempTaxes = priceParse * 0.2
        totalTaxes += priceParse * 0.2
        totalPrice += (priceParse + tempTaxes)
    price = input()

if price == "special":
    totalPrice -= (totalPrice * 0.1)

if totalPrice == 0:
    print (f"Invalid order!")
else:
    print (f"Congratulations you've just bought a new computer!\nPrice without taxes: {(priceWoTaxes):.2f}$\nTaxes: {totalTaxes:.2f}$\n{'-' * 11}\n\
Total price: {(totalPrice):.2f}$")