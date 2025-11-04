#Pizza Orders

orders = [int(i) for i in input().split(', ')]
capacities = [int(i) for i in input().split(', ')]

totalPizzas = 0

while orders and capacities:
    currentOrder = orders[0]
    currentCapacity = capacities[-1]

    if currentOrder > 10 or currentOrder <= 0:
        orders.pop(0)
        continue
    
    if currentOrder <= currentCapacity:
        totalPizzas += currentOrder
        orders.pop(0)
        capacities.pop()

    elif currentOrder > currentCapacity:
        totalPizzas += currentCapacity
        capacities.pop()
        orders[0] = currentOrder - currentCapacity

if not orders and capacities:
    print (f"All orders are successfully completed!\nTotal pizzas made: {totalPizzas}\nEmployees: {', '.join(map(str, capacities))}")
else:
    print (f"Not all orders are completed.\nOrders left: {', '.join(map(str, orders))}")
