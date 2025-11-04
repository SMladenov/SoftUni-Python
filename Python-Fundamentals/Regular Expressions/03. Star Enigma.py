#Star Enigma

import re

messages = int(input())

listAttackedPlanets = []
listDestroyedPlanets = []

for message in range (messages):
    cmd = input()
    
    lenStar = 0
    patternStar = r"[sStTaArR]+"
    listStar = re.findall(patternStar, cmd)
    for i in listStar:
        lenStar += len(i)
    
    decrypted = ""
    for i in cmd:
        dec = ord(i)
        char = chr(dec - lenStar)
        decrypted += char
    
    #print (f"{decrypted}")
    
    patternPlanet = r"(?<=\@)[a-zA-Z]+(?=[^a-zA-Z\@\-\!\:\>]*:)"
    patternPopulation = r"(?<=\:)\d+(?=\!)"
    patternAttack = r"(?<=\!)[AD](?=\!)"
    patternSoldier = r"(?<=\-\>)\d+"
    
    listPlanet = re.findall(patternPlanet, decrypted)
    listPopulation = re.findall(patternPopulation, decrypted)
    listAttack = re.findall(patternAttack, decrypted)
    listSoldier = re.findall(patternSoldier, decrypted)
    
    if listPlanet and listPopulation and listAttack and listSoldier:
        if listAttack[0] == "A":
            listAttackedPlanets.append(listPlanet[0])
        elif listAttack[0] == "D":
            listDestroyedPlanets.append(listPlanet[0])
        #print (f"{listPlanet[0]} => {listPopulation[0]} => {listAttack[0]} => {listSoldier[0]}")

print (f"Attacked planets: {len(listAttackedPlanets)}")
if listAttackedPlanets:
    listAttackedPlanets.sort()
    for i in listAttackedPlanets:
        print (f"-> {i}")
print (f"Destroyed planets: {len(listDestroyedPlanets)}")
if listDestroyedPlanets:
    listDestroyedPlanets.sort()
    for i in listDestroyedPlanets:
        print (f"-> {i}")