#Easter Gifts

gifts = input().split(' ')

cmd = input()

while cmd != "No Money":
    cmdSplit = cmd.split(' ')
    if cmdSplit[0] == "OutOfStock":
        for index, i in enumerate(gifts):
            if i == cmdSplit[1]:
                gifts[index] = None
    if cmdSplit[0] == "Required":
        if 0 <= int(cmdSplit[2]) <= (len(gifts) - 1):
            gifts[int(cmdSplit[2])] = cmdSplit[1]
    if cmdSplit[0] == "JustInCase":
        gifts[len(gifts) - 1] = cmdSplit[1]
    cmd = input()

for i in gifts:
    if i != None:
        print (f"{i}", end = " ")
        