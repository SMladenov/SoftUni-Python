#Secret Chat

message = input()

cmd = input()

while cmd != "Reveal":
    cmdSplit = cmd.split(':|:')
    action = cmdSplit[0]
    if action == "InsertSpace":
        index = int(cmdSplit[1])
        message = message[:index] + " " + message[index:]
        print (f"{message}")
    if action == "Reverse":
        substring = cmdSplit[1]
        if substring in message:
            message = message.replace(substring, "", 1)
            subReverse = substring[::-1]
            message = message + subReverse
            print (f"{message}")
        else:
            print (f"error")
    if action == "ChangeAll":
        substring = cmdSplit[1]
        replacestring = cmdSplit[2]
        message = message.replace(substring, replacestring)
        print (f"{message}")
    cmd = input()

print (f"You have a new text message: {message}")