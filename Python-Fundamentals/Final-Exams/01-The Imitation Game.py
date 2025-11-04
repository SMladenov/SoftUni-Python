#The Imitation Game

message = input()

cmd = input()

while cmd != "Decode":
    cmdSplit = cmd.split('|')
    action = cmdSplit[0]
    if action == "Move":
        numOfLetters = int(cmdSplit[1])
        message = message[numOfLetters:] + message[:numOfLetters]
    if action == "Insert":
        index = int(cmdSplit[1])
        value = cmdSplit[2]
        message = message[:index] + value + message[index:]
    if action == "ChangeAll":
        substring = cmdSplit[1]
        replacement = cmdSplit[2]
        message = message.replace(substring, replacement)
    cmd = input()

print (f"The decrypted message is: {message}")