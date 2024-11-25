#Coffee Lover

coffees = input().split(' ')
numberCmd = int(input())

for i in range (numberCmd):
    cmd = input()
    cmdSplit = cmd.split(' ')
    action = cmdSplit[0]
    if action == "Include":
        coffee = cmdSplit[1]
        coffees.append(coffee)
    if action == "Remove":
        secondAction = cmdSplit[1]
        number = int(cmdSplit[2])
        if number < len(coffees):
            if secondAction == "first":
                for i in range (number):
                    coffees.remove(coffees[0])
            if secondAction == "last":
               for i in range (number):
                    coffees.remove(coffees[len(coffees) - 1])
    if action == "Prefer":
        index1 = int(cmdSplit[1])
        index2 = int(cmdSplit[2])
        if (0 <= index1 < len(coffees)) and (0 <= index2 < len(coffees)):
            value1 = coffees[index1]
            value2 = coffees[index2]
            coffees[index1] = value2
            coffees[index2] = value1
    if action == "Reverse":
        coffees.reverse()

print (f"Coffees:\n{' '.join(coffees)}")
