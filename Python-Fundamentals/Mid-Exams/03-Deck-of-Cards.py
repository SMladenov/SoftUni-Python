#Deck of Cards

cards = input().split(', ')
numberCmd = int(input())

for i in range (numberCmd):
    cmd = input()
    cmdSplit = cmd.split(', ')
    action = cmdSplit[0]
    if action == "Add":
        card = cmdSplit[1]
        if card in cards:
            print (f"Card is already in the deck")
        else:
            cards.append(card)
            print (f"Card successfully added")
    if action == "Remove":
        card = cmdSplit[1]
        if card not in cards:
            print (f"Card not found")
        else:
            cards.remove(card)
            print (f"Card successfully removed")
    if action == "Remove At":
        index = int(cmdSplit[1])
        if 0 <= index < len(cards):
            cards.pop(index)
            print (f"Card successfully removed")
        else:
            print (f"Index out of range")
    if action == "Insert":
        index = int(cmdSplit[1])
        card = cmdSplit[2]
        if 0 <= index < len(cards):
            if card in cards:
                print (f"Card is already added")
            else:
                cards.insert(index, card)
                print (f"Card successfully added")
        else:
            print (f"Index out of range")

print (f"{', '.join(cards)}")