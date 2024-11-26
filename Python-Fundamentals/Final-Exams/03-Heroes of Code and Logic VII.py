#Heroes of Code and Logic VII

heroesNumber = int(input())

dicHeroes = {}

for i in range (heroesNumber):
    cmdHeroes = input().split(' ')
    name = cmdHeroes[0]
    hp = int(cmdHeroes[1])
    mp = int(cmdHeroes[2])
    if name not in dicHeroes.keys():
        dicHeroes[name] = {'hp': hp, 'mp': mp}
        if hp > 100:
            dicHeroes[name]['hp'] = 100
        if mp > 200:
            dicHeroes[name]['mp'] = 200

cmd = input()

while cmd != "End":
    cmdSplit = cmd.split(' - ')
    action = cmdSplit[0]
    name = cmdSplit[1]

    if action == "CastSpell":
        mpNeeded = int(cmdSplit[2])
        spellName = cmdSplit[3]
        if dicHeroes[name]['mp'] - mpNeeded >= 0:
            dicHeroes[name]['mp'] = dicHeroes[name]['mp'] - mpNeeded
            print (f"{name} has successfully cast {spellName} and now has {dicHeroes[name]['mp']} MP!")
        else:
            print (f"{name} does not have enough MP to cast {spellName}!")

    if action == "TakeDamage":
        hpTaken = int(cmdSplit[2])
        attacker = cmdSplit[3]
        dicHeroes[name]['hp'] = dicHeroes[name]['hp'] - hpTaken
        if dicHeroes[name]['hp'] <= 0:
            print (f"{name} has been killed by {attacker}!")
            dicHeroes.pop(name)
        else:
            print (f"{name} was hit for {hpTaken} HP by {attacker} and now has {dicHeroes[name]['hp']} HP left!")

    if action == "Recharge":
        mpToRecharge = int(cmdSplit[2])
        if dicHeroes[name]['mp'] + mpToRecharge > 200:
            print (f"{name} recharged for {200 - dicHeroes[name]['mp']} MP!")
            dicHeroes[name]['mp'] = 200
        else:
            dicHeroes[name]['mp'] = dicHeroes[name]['mp'] + mpToRecharge
            print (f"{name} recharged for {mpToRecharge} MP!")

    if action == "Heal":
        hpToHeal = int(cmdSplit[2])
        if dicHeroes[name]['hp'] + hpToHeal > 100:
            print (f"{name} healed for {100 - dicHeroes[name]['hp']} HP!")
            dicHeroes[name]['hp'] = 100
        else:
            dicHeroes[name]['hp'] = dicHeroes[name]['hp'] + hpToHeal
            print (f"{name} healed for {hpToHeal} HP!")
    cmd = input()

for key, value in dicHeroes.items():
    print (f"{key}\n  HP: {value['hp']}\n  MP: {value['mp']}")