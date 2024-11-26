#Nether Realms

import re

#demons = re.split(r',\s*', input().strip())
demons = input().split(',')
demons = [i.strip() for i in demons if i.strip()]
demons.sort()

for demon in demons:
    patternHealth = r"[^\d+\+\-\*\/\.]"
    patternDamage = r"[-]?\d+(?:\.\d+)?"

    listHealth = re.findall(patternHealth, demon)
    listDamage = re.findall(patternDamage, demon)
    
    totalHealth = sum(ord(i) for i in listHealth)
    totalDamage = sum(float(i) for i in listDamage)

    countMultiply = demon.count('*')
    countDivide = demon.count('/')

    for i in range (countMultiply):
        totalDamage *= 2
    for i in range (countDivide):
        totalDamage /= 2
    
    print (f"{demon} - {totalHealth} health, {totalDamage:.2f} damage")