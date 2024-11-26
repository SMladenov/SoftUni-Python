#Trains

wagons = int(input())
train = []
for i in range (wagons):
    train.append(0)

cmd = input()

while cmd != "End":
    cmdSplit = cmd.split(' ')
    action = cmdSplit[0]
    if action == "add":
        train[len(train) - 1] += int(cmdSplit[1])
    if action == "insert":
        train[int(cmdSplit[1])] += int(cmdSplit[2])
    if action == "leave":
        train[int(cmdSplit[1])] -= int(cmdSplit[2])
    cmd = input()

print (f"{train}")