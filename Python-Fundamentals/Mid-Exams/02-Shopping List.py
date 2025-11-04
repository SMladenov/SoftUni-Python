#Shopping List

shoppingList = input().split('!')
cmd = input()

while cmd != "Go Shopping!":
    cmdSplit = cmd.split(' ')
    action = cmdSplit[0]
    if action == "Urgent":
        item = cmdSplit[1]
        if item not in shoppingList:
            shoppingList.insert(0, item)
    if action == "Unnecessary":
        item = cmdSplit[1]
        if item in shoppingList:
            shoppingList.remove(item)
    if action == "Correct":
        oldItem = cmdSplit[1]
        newItem = cmdSplit[2]
        if oldItem in shoppingList:
            indexOld = shoppingList.index(oldItem)
            shoppingList[indexOld] = newItem
    if action == "Rearrange":
        item = cmdSplit[1]
        if item in shoppingList:
            shoppingList.remove(item)
            shoppingList.append(item)
    cmd = input()

print (f"{', '.join(shoppingList)}")