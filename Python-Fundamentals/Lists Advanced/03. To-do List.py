#To-do List

toDoList = [""] * 10

cmd = input()

while cmd != "End":
    cmdSplit = cmd.split('-')
    index = int(cmdSplit[0]) - 1
    toDoList.pop(index)
    toDoList.insert(index, cmdSplit[1])
    cmd = input()

toDoList = [i for i in toDoList if i != ""]

print (f"{toDoList}")