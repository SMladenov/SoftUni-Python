#Numbers

numbers = input().split(' ')
cmd = input()

while cmd != "Finish":
    cmdSplit = cmd.split(' ')
    action = cmdSplit[0]
    if action == "Add":
        value = cmdSplit[1]
        numbers.append(value)
    if action == "Remove":
        value = cmdSplit[1]
        if value in numbers:
            numbers.remove(value)
    if action == "Replace":
        value1 = cmdSplit[1]
        value2 = cmdSplit[2]
        if value1 in numbers:
            index1 = numbers.index(value1)
            numbers[index1] = value2
    if action == "Collapse":
        value = int(cmdSplit[1])
        numbers = [i for i in numbers if int(i) > value]
    cmd = input()

print (f"{' '.join(numbers)}")