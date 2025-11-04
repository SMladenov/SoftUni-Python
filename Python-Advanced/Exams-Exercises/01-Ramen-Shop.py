#Ramen Shop

bowls = [int(i) for i in input().split(', ')]
customers = [int(i) for i in input().split(', ')]

while bowls and customers:
    currentBowl = bowls[-1]
    currentCustomer = customers[0]

    if currentBowl == currentCustomer:
        bowls.pop()
        customers.pop(0)
    elif currentBowl > currentCustomer:
        bowls[-1] -= currentCustomer
        customers.pop(0)
        
    elif currentCustomer > currentBowl:
        customers[0] -= currentBowl
        bowls.pop()
        
if not customers:
    print (f"Great job! You served all the customers.")
    if bowls:
        print (f"Bowls of ramen left: {', '.join(map(str, bowls))}")
if customers:
    print (f"Out of ramen! You didn't manage to serve all customers.")
    print (f"Customers left: {', '.join(map(str, customers))}")
