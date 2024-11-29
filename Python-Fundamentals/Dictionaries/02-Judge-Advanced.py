#Judge

cmd = input()

dicContests = {}
orderInput = []

while cmd != "no more time":
    cmdSplit = cmd.split('->')
    cmdSplit = [i.strip() for i in cmdSplit if i.strip()]
    username = cmdSplit[0]
    contest = cmdSplit[1]
    points = int(cmdSplit[2])
    if contest not in dicContests.keys():
        dicContests[contest] = {username: points}
        orderInput.append(contest)
    else:
        if username not in dicContests[contest].keys():
            dicContests[contest][username] = points
        else:
            if points > dicContests[contest][username]:
                dicContests[contest][username] = points
    cmd = input()

allPointsAndUsers = {}

for contest in orderInput:
    print (f"{contest}: {len(dicContests[contest])} participants")
    counter = 0
    # Sort by total points (descending) and then by username (ascending)
    for user, points in sorted(dicContests[contest].items(), key=lambda x: (-x[1], x[0])):
        counter += 1
        if user not in allPointsAndUsers.keys():
            allPointsAndUsers[user] = points
        else:
            allPointsAndUsers[user] += points
        print (f"{counter}. {user} <::> {points}")

print (f"Individual standings:")
counter2 = 0
# Sort by total points (descending) and then by username (ascending)
for user, points in sorted(allPointsAndUsers.items(), key=lambda x: (-x[1], x[0])):
    counter2 += 1
    print (f"{counter2}. {user} -> {points}")
