#MOBA Challenger

dicPlayers = {}

cmd = input()

while cmd != "Season end":
    cmdSplit1 = cmd.split(' -> ')
    if len(cmdSplit1) > 1:
        player = cmdSplit1[0]
        position = cmdSplit1[1]
        skill = int(cmdSplit1[2])
        if player not in dicPlayers.keys():
            dicPlayers[player] = {position: skill}
        else:
            if position not in dicPlayers[player].keys():
                dicPlayers[player][position] = skill
            else:
                if skill > dicPlayers[player][position]:
                    dicPlayers[player][position] = skill
    if len(cmdSplit1) <= 1:
        cmdSplit2 = cmd.split(' vs ')
        player1 = cmdSplit2[0]
        player2 = cmdSplit2[1]
        if player1 in dicPlayers.keys() and player2 in dicPlayers.keys():
            skillPlayer1 = sum(dicPlayers[player1].values())
            skillPlayer2 = sum(dicPlayers[player2].values())
            for position in dicPlayers[player1].keys():
                if position in dicPlayers[player2].keys():
                    if skillPlayer1 > skillPlayer2:
                        dicPlayers.pop(player2)
                        break
                    else:
                        dicPlayers.pop(player1)
                        break
    cmd = input()


playersTotalSkills = {player: sum(skill.values()) for player, skill in dicPlayers.items()}

for player, totalSkill in sorted(playersTotalSkills.items(), key=lambda x: (-x[1], x[0])):
    print (f"{player}: {totalSkill} skill")
    for position, skill in sorted(dicPlayers[player].items(), key=lambda x: (-x[1], x[0])):
        print (f"- {position} <::> {skill}")

#for player, value in dicPlayers.items():
#    print (f"{player}: To Be Added")
#    for position, skill in value.items():
#        print (f"- {position} <::> {skill}")
