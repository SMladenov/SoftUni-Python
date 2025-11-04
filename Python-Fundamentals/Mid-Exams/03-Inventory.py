#Inventory

items = input().split(', ')

cmd = input()

while cmd != "Craft!":
    cmdSplit = cmd.split(' - ')
    action = cmdSplit[0]
    item = cmdSplit[1]
    if action == "Collect":
        if item not in items:
            items.append(item)
    elif action == "Drop":
        if item in items:
            items.remove(item)
    elif action == "Combine Items":
        itemSplit = item.split(':')
        oldItem = itemSplit[0]
        newItem = itemSplit[1]
        if oldItem in items:
            index = items.index(oldItem)
            items.insert(index + 1, newItem)
    elif action == "Renew":
        if item in items:
            items.remove(item)
            items.append(item)
    cmd = input()

print (f"{', '.join(items)}")