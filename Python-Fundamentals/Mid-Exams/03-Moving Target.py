#Moving Target

targets = [int(i) for i in input().split(' ')]

cmd = input()

while cmd != "End":
    cmdSplit = cmd.split(' ')
    action = cmdSplit[0]
    index = int(cmdSplit[1])
    
    if action == "Shoot":
        power = int(cmdSplit[2])
        if 0 <= index < len(targets):
            targets[index] -= power
            if targets[index] <= 0:
                targets.pop(index)
    if action == "Add":
        value = int(cmdSplit[2])
        if 0 <= index < len(targets):
            targets.insert(index, value)
        else:
            print (f"Invalid placement!")
    if action == "Strike":
        radius = int(cmdSplit[2])
        strikeIndex1 = index - radius
        strikeIndex2 = index + radius
        if 0 <= index < len(targets):
            if strikeIndex1 >= 0 and strikeIndex2 < len(targets):
                targets = targets[:strikeIndex1] + targets[strikeIndex2 + 1:]
            else:
                print (f"Strike missed!")
    cmd = input()

print (f"{'|'.join(map(str, targets))}")