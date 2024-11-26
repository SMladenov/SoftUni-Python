#The Pianist

numberPieces = int(input())

dicPieces = {}

for i in range (numberPieces):
    piecesSplit = input().split('|')
    piece = piecesSplit[0]
    composer = piecesSplit[1]
    key = piecesSplit[2]
    if piece not in dicPieces.keys():
        dicPieces[piece] = {'composer': composer, 'key': key}

cmd = input()

while cmd != "Stop":
    cmdSplit = cmd.split('|')
    action = cmdSplit[0]
    piece = cmdSplit[1]
    if action == "Add":
        if piece not in dicPieces.keys():
            composer = cmdSplit[2]
            key = cmdSplit[3]
            dicPieces[piece] = {'composer': composer, 'key': key}
            print (f"{piece} by {composer} in {key} added to the collection!")
        else:
            print (f"{piece} is already in the collection!")
    if action == "Remove":
        if piece in dicPieces.keys():
            dicPieces.pop(piece)
            print (f"Successfully removed {piece}!")
        else:
            print (f"Invalid operation! {piece} does not exist in the collection.")
    if action == "ChangeKey":
        newKey = cmdSplit[2]
        if piece in dicPieces.keys():
            dicPieces[piece]['key'] = newKey
            print (f"Changed the key of {piece} to {newKey}!")
        else:
            print (f"Invalid operation! {piece} does not exist in the collection.")
    cmd = input()

for key, value in dicPieces.items():
    print (f"{key} -> Composer: {value['composer']}, Key: {value['key']}")