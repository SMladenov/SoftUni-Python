#Phonebook

cmd = input()

dictPhonebook = {}

while not cmd.isdigit():
    cmdSplit = cmd.split('-')
    name = cmdSplit[0]
    phone = cmdSplit[1]
    dictPhonebook[name] = phone
    cmd = input()

if cmd.isdigit():
    for i in range (int(cmd)):
        search = input()
        if search in dictPhonebook.keys():
            print (f"{search} -> {dictPhonebook[search]}")
        else:
            print (f"Contact {search} does not exist.")