#Cupcake-Shop

def stock_availability (*args):
    listFlavours = list(args[0])
    cmd = args[1]
    otherParameters = []
    
    if len(args) > 2:
        otherParameters = list(map(str, args[2:]))

    if cmd == "delivery":
        listFlavours.extend(otherParameters)
        return listFlavours

    elif cmd == "sell":
        if otherParameters:
            if len(otherParameters) == 1 and otherParameters[0].isdigit():
                listFlavours = listFlavours[int(otherParameters[0]):]
                return listFlavours
            else:
                for order in otherParameters:
                    if order in listFlavours:
                        while order in listFlavours:
                            listFlavours.remove(order)
                return listFlavours
            
        else:
            listFlavours = listFlavours[1:]
            return listFlavours
    
print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
