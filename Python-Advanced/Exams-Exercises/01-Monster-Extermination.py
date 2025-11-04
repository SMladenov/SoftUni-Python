#Monster Extermination

armor = [int(i) for i in input().split(',')]
damage = [int(i) for i in input().split(',')]

monstersKilled = 0

while armor and damage:
    
    currentArmor = armor.pop(0)
    currentDamage = damage.pop(-1)

    if currentDamage >= currentArmor:
        monstersKilled += 1
        monsterIsDead = True
        remainingDamage = currentDamage - currentArmor
        
        if remainingDamage > 0:
            if damage:
                damage[-1] += remainingDamage
            else:
                damage.append(remainingDamage)

    else:
        currentArmor -= currentDamage
        armor.append(currentArmor)
                
if not armor:
    print (f"All monsters have been killed!")
if not damage:
    print (f"The soldier has been defeated.")
print (f"Total monsters killed: {monstersKilled}")
           