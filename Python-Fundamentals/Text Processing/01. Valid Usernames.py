#Valid Usernames

def validationUsername (username):
    listValidSymbols = ['-', '_']
    isValid = True
    if 3 <= len(username) <= 16:
        for i in username:
            if not (i.isdigit() or i.isalpha() or i in listValidSymbols):
                isValid = False
                break
    else:
        isValid = False
    return isValid

usernames = input().split(', ')

validOnes = [i for i in usernames if validationUsername(i)]

print ('\n'.join(validOnes))