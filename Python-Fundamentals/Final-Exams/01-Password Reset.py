#Password Reset

password = input()

cmd = input()

while cmd != "Done":
    cmdSplit = cmd.split(' ')
    action = cmdSplit[0]
    takeOdd = ""
    
    if action == "TakeOdd":
        for index, i in enumerate(password):
            if index % 2 == 1:
                takeOdd += i
            password = takeOdd
        print (f"{password}")

    if action == "Cut":
        index = int(cmdSplit[1])
        length = int(cmdSplit[2])
        password = password[:index] + password[index + length:]
        print (f"{password}")

    if action == "Substitute":
        substring = cmdSplit[1]
        substitute = cmdSplit[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print (f"{password}")
        else:
            print (f"Nothing to replace!")
    cmd = input()

print (f"Your password is: {password}")