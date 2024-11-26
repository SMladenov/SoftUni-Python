#Orders

numberOfOrders = int(input())

totalPrice = 0
allConditionsMet = True

for i in range (numberOfOrders):
    allConditionsMet = True
    pricePerCapsule = float(input())
    if pricePerCapsule < 0.01 or pricePerCapsule > 100.00:
        allConditionsMet = False
    days = int(input())
    if days < 1 or days > 31:
        allConditionsMet = False
    capsulesNeeded = int(input())
    if capsulesNeeded < 1 or capsulesNeeded > 2000:
        allConditionsMet = False
        
    if allConditionsMet:
        priceForOrder = pricePerCapsule * days * capsulesNeeded
        totalPrice += priceForOrder
        print (f"The price for the coffee is: ${priceForOrder:.2f}")

print (f"Total: ${totalPrice:.2f}")
