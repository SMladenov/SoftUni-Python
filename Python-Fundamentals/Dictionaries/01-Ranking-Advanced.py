#Ranking

dicContests = {}
dicUsers = {}

cmd1 = input()

while cmd1 != "end of contests":
    cmd1Split = cmd1.split(':')
    contest = cmd1Split[0]
    password = cmd1Split[1]
    if contest not in dicContests.keys():
        dicContests[contest] = password
    cmd1 = input()

cmd2 = input()

while cmd2 != "end of submissions":
    cmd2Split = cmd2.split('=>')
    contest = cmd2Split[0]
    password = cmd2Split[1]
    username = cmd2Split[2]
    points = int(cmd2Split[3])

    #Check if contest is valid and append the record
    if contest in dicContests.keys() and password == dicContests[contest]:
        if username not in dicUsers.keys():
            dicUsers[username] = {contest: points}
        else:
            if contest not in dicUsers[username].keys():
                dicUsers[username][contest] = points
            else:
                if points > dicUsers[username][contest]:
                    dicUsers[username][contest] = points
    cmd2 = input()

#Find who is with max points
usersTotalPoints = {user: sum(points.values()) for user, points in dicUsers.items()}
#Use it to compare the maximum value, instead we will compare the keys
userMax = max(usersTotalPoints, key=usersTotalPoints.get)
pointsMax = usersTotalPoints[userMax]
print(f"Best candidate is {userMax} with total {pointsMax} points.")
print(f"Ranking:")

for user in sorted(dicUsers.keys()):
    print(f"{user}")
    # Print contests sorted by points in descending order
    #x is each tuple in the items() key - value, represented in tuple (x[1] is the second element of the tuple)
    for contest, points in sorted(dicUsers[user].items(), key=lambda x: -x[1]):
        print(f"#  {contest} -> {points}")

#for key, value in dicUsers.items():
#    print (f"{key}")
#    for key2, value2 in value.items():
#        print (f"# {key2} -> {value2}")
            