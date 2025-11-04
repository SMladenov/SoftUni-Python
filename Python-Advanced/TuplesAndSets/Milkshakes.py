#Milkshakes

chocolates = [int(i) for i in input().strip().split(', ')]
cupsOfMilk = [int(i) for i in input().strip().split(', ')]

counterMilkshakes = 0

while True:
    oneIsRemoved = False
    
    if counterMilkshakes == 5:
        print (f"Great! You made all the chocolate milkshakes needed!")
        if cupsOfMilk and chocolates:
            print (f"Chocolate: {', '.join(map(str, chocolates))}\nMilk: {', '.join(map(str, cupsOfMilk))}")
            break
        if not cupsOfMilk and not chocolates:
            print (f"Chocolate: empty\nMilk: empty")
            break
        if not cupsOfMilk and chocolates:
            print (f"Milk: empty\nChocolate: {', '.join(map(str, chocolates))}")
            break
        if not chocolates and cupsOfMilk:
            print (f"Chocolate: empty\nMilk: {', '.join(map(str, cupsOfMilk))}")
            break
        
    if chocolates and cupsOfMilk:
        tempChocolate = chocolates[len(chocolates) - 1]
        tempMilk = cupsOfMilk[0]

        if tempChocolate <= 0:
            chocolates.pop(len(chocolates) - 1)
            oneIsRemoved = True
        if tempMilk <= 0:
            cupsOfMilk.pop(0)
            oneIsRemoved = True

        if not chocolates:
            if cupsOfMilk:
                print (f"Not enough milkshakes.\nChocolate: empty\nMilk: {', '.join(map(str, cupsOfMilk))}")
                break
            else:
                print (f"Not enough milkshakes.\nChocolate: empty\nMilk: empty")
                break
        
        if not cupsOfMilk:
            if chocolates:
                print (f"Not enough milkshakes.\nChocolate: {', '.join(map(str, chocolates))}\nMilk: empty")
                break
            else:
                print (f"Not enough milkshakes.\nChocolate: empty\nMilk: empty")
                break
                
        if tempChocolate == tempMilk and not oneIsRemoved:
            counterMilkshakes += 1
            chocolates.pop(len(chocolates) - 1)
            cupsOfMilk.pop(0)
        elif tempChocolate != tempMilk and not oneIsRemoved:
            tempCup = cupsOfMilk.pop(0)
            cupsOfMilk.append(tempCup)
            chocolates[len(chocolates) - 1] -= 5
