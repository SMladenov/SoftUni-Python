#Bakery Shop

dicStock = {}

soldItems = 0

cmd = input()

while cmd != "Complete":
    cmdSplit = [i.strip() for i in cmd.split(' ') if i.strip()]
    action = cmdSplit[0]
    quantity = int(cmdSplit[1])
    food = cmdSplit[2]
    if action == "Receive":
        if quantity > 0:
            if food not in dicStock.keys():
                dicStock[food] = quantity
            else:
                dicStock[food] += quantity
    if action == "Sell":
        if food not in dicStock.keys():
            print (f"You do not have any {food}.")
        else:
            if (dicStock[food] - quantity) < 0:
                print (f"There aren't enough {food}. You sold the last {dicStock[food]} of them.")
                soldItems += dicStock[food]
                dicStock.pop(food)
            else:
                dicStock[food] -= quantity
                print (f"You sold {quantity} {food}.")
                soldItems += quantity
                if dicStock[food] == 0:
                    dicStock.pop(food)
    cmd = input()

for key, value in dicStock.items():
    print (f"{key}: {value}")
print (f"All sold: {soldItems} goods")
