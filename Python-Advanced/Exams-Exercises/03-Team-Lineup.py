#Team-Lineup

def team_lineup (*args):
    
    dicPlayers = {}
    
    for player, country in args:
        if country not in dicPlayers.keys():
            dicPlayers[country] = [player]
        else:
            dicPlayers[country].append(player)

    dicPlayersSorted = dict(sorted(dicPlayers.items(), key=lambda x: (-len(x[1]), x[0])))

    listToPrint = []

    for country, players in dicPlayersSorted.items():
        listToPrint.append(f"{country}:")
        for player in players:
            listToPrint.append(f"  -{player}")

    return '\n'.join(listToPrint)

print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany"),
   ("Bruno Fernandes", "Portugal"),
   ("Bernardo Silva", "Portugal"),
   ("Harry Maguire", "England")))
