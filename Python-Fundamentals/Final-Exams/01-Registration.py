#Registration

username = input()

cmd = input()

while cmd != "Registration":
    cmdSplit = cmd.split(' ')
    action = cmdSplit[0]
    if action == "Letters":
        if cmdSplit[1] == "Lower":
            username = username.lower()
            print (f"{username}")
        else:
            username = username.upper()
            print (f"{username}")
    elif action == "Reverse":
        startIndex = int(cmdSplit[1])
        endIndex = int(cmdSplit[2])
        if 0 <= startIndex < len(username) and 0 <= endIndex < len(username):
            substring = username[startIndex:endIndex + 1][::-1]
            print (f"{substring}")
    elif action == "Substring":
        substring = cmdSplit[1]
        if substring in username:
            username = username.replace(substring, "")
            print (f"{username}")
        else:
            print (f"The username {username} doesn't contain {substring}.")
    elif action == "Replace":
        char = cmdSplit[1]
        username = username.replace(char, '-')
        print (f"{username}")
    elif action == "IsValid":
        char = cmdSplit[1]
        if char in username:
            print (f"Valid username.")
        else:
            print (f"{char} must be contained in your username.")
    cmd = input()