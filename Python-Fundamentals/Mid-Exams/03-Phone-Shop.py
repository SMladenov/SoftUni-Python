#Phone Shop

phones = input().split(', ')

cmd = input()

while cmd != "End":
    cmdSplit = cmd.split('-')
    cmdSplit = [i.strip() for i in cmdSplit if i.strip()]
    action = cmdSplit[0]
    if action == "Add":
        phone = cmdSplit[1]
        if phone not in phones:
            phones.append(phone)
    if action == "Remove":
        phone = cmdSplit[1]
        if phone in phones:
            phones.remove(phone)
    if action == "Bonus phone":
        phones2 = cmdSplit[1].split(':')
        oldPhone = phones2[0]
        newPhone = phones2[1]
        if oldPhone in phones:
            indexOldPhone = phones.index(oldPhone)
            phones.insert(indexOldPhone + 1, newPhone)
    if action == "Last":
        phone = cmdSplit[1]
        if phone in phones:
            phones.remove(phone)
            phones.append(phone)
    cmd = input()

print (f"{', '.join(phones)}")