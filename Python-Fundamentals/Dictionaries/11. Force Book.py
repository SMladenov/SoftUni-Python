#Force Book

def checkUser (dicSides, user):
    for value in dicSides.values():
        for item in value:
            if item == user:
                return True
    return False

cmd = input()

dicSides = {}

while cmd != "Lumpawaroo":
    cmdSplit1 = cmd.split(' | ')
    cmdSplit2 = cmd.split(' -> ')
    
    #Case Side | User
    if len(cmdSplit1) > 1:
        side = cmdSplit1[0]
        user = cmdSplit1[1]
        
        if not checkUser(dicSides, user):
            if side not in dicSides:
                dicSides[side] = []  
            dicSides[side].append(user) 

    #Case User -> Side
    if len(cmdSplit2) > 1:
        user = cmdSplit2[0]
        side = cmdSplit2[1]
        
        if side in dicSides.keys():
            if checkUser(dicSides, user):
                for key, value in dicSides.items():
                    if user in value:
                        dicSides[key].remove(user)
                dicSides[side].append(user)
                print (f"{user} joins the {side} side!")
            if not checkUser(dicSides, user):
                dicSides[side].append(user)
                print (f"{user} joins the {side} side!")
        
        if side not in dicSides.keys():
            if checkUser(dicSides, user):
                for key, value in dicSides.items():
                    if user in value:
                        dicSides[key].remove(user)
                dicSides[side] = []
                dicSides[side].append(user)
                print (f"{user} joins the {side} side!")
            if not checkUser(dicSides, user):
                dicSides[side] = []
                dicSides[side].append(user)
                print (f"{user} joins the {side} side!")
    cmd = input()

for key, value in dicSides.items():
    if len(value) > 0:
        print (f"Side: {key}, Members: {len(value)}")
        print ('\n'.join(f"! {i}" for i in value))