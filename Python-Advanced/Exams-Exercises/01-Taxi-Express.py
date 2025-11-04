#Taxi Express

customers = [int(i) for i in input().split(', ')]
taxis = [int(i) for i in input().split(', ')]

totalTime = 0

while customers and taxis:
    currentCustomer = customers[0]
    currentTaxi = taxis[-1]

    if currentTaxi >= currentCustomer:
        totalTime += currentCustomer
        customers.pop(0)
        taxis.pop()
    else:
        taxis.pop()

if not customers:
    print (f"All customers were driven to their destinations\nTotal time: {totalTime} minutes")
else:
    print (f"Not all customers were driven to their destinations\nCustomers left: {', '.join(map(str, customers))}")
