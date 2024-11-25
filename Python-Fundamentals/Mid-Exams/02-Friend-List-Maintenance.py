#Friend List Maintenance

friends = input().split(', ')
cmd = input()

while cmd != "Report":
    cmdSplit = cmd.split(' ')
    action = cmdSplit[0]

    if action == "Blacklist":
        name = cmdSplit[1]
        if name in friends:
            index = friends.index(name)
            friends[index] = "Blacklisted"
            print (f"{name} was blacklisted.")
        else:
            print (f"{name} was not found.")
    if action == "Error":
        index = int(cmdSplit[1])
        if 0 <= index < len(friends):
            name = friends[index]
            if name != "Blacklisted" and name != "Lost":
                friends[index] = "Lost"
                print (f"{name} was lost due to an error.")
    if action == "Change":
        index = int(cmdSplit[1])
        newName = cmdSplit[2]
        if 0 <= index < len(friends):
            oldName = friends[index]
            friends[index] = newName
            print (f"{oldName} changed his username to {newName}.")
    cmd = input()

blacklisted = [i for i in friends if i == "Blacklisted"]
print (f"Blacklisted names: {len(blacklisted)}")

lost = [i for i in friends if i == "Lost"]
print (f"Lost names: {len(lost)}")

print (f"{' '.join(friends)}")
