#Fast Food
#Queue

foodQuantity = int(input())
foodOrders = [int(i) for i in input().strip().split(' ') if i.strip()]
print (f"{max(foodOrders)}")

while foodOrders:
    if foodQuantity - foodOrders[0] >= 0:
        foodQuantity -= foodOrders.pop(0)
    else:
        break

if foodOrders:
    print (f"Orders left: {' '.join(map(str, foodOrders))}")
else:
    print (f"Orders complete")
