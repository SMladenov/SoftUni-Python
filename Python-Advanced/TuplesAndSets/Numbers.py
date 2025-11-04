#Numbers

list1 = set([int(i) for i in input().strip().split()])
list2 = set([int(i) for i in input().strip().split()])

numberCommands = int(input())

for _ in range (numberCommands):
    cmdSplit = input().strip().split()
    action = f"{cmdSplit[0]} {cmdSplit[1]}"
    numbers = [int(cmdSplit[i]) for i in range (2, len(cmdSplit))]

    if action == "Add First":
        for i in numbers:
            list1.add(i)
    if action == "Add Second":
        for i in numbers:
            list2.add(i)
    if action == "Remove First":
        for i in numbers:
            list1.discard(i)
    if action == "Remove Second":
        for i in numbers:
            list2.discard(i)
    if action == "Check Subset":
        isSubset1 = list1.issubset(list2)
        isSubset2 = list2.issubset(list1)
        if isSubset1 or isSubset2:
            print (True)
        else:
            print (False)

print (f"{', '.join(map(str, sorted(list1)))}\n{', '.join(map(str, sorted(list2)))}")
