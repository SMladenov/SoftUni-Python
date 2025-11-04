#Chat Logger

chat = []
cmd = input()

while cmd != "end":
    cmdSplit = cmd.split(' ')
    action = cmdSplit[0]
    if action == "Chat":
        message = cmdSplit[1]
        chat.append(message)
    if action == "Delete":
        message = cmdSplit[1]
        if message in chat:
            chat.remove(message)
    if action == "Edit":
        message = cmdSplit[1]
        messageEdit = cmdSplit[2]
        if message in chat:
            index = chat.index(message)
            chat[index] = messageEdit
    if action == "Pin":
        message = cmdSplit[1]
        if message in chat:
            chat.remove(message)
            chat.append(message)
    if action == "Spam":
        messages = [cmdSplit[i] for i in range (1, len(cmdSplit))]
        chat += messages
    cmd = input()

for i in chat:
    print (f"{i}")
