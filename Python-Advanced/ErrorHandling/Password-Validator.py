#Password Validator

class PasswordTooShortError(Exception):
    pass

class PasswordTooCommonError(Exception):
    pass

class PasswordNoSpecialCharactersError(Exception):
    pass

class PasswordContainsSpacesError(Exception):
    pass

def passwordLength(password):
    if len(password) < 8:
        return False
    else:
        return True

def passwordSpecialCharacter(password):
    listChar = ['@', '*', '&', '%']
    specialFound = False
    for i in password:
        if i in listChar:
            specialFound = True
            break
    return specialFound

def passwordSpace(password):
    spaceFound = False
    for i in password:
        if i == " ":
            spaceFound = True
            break
    return spaceFound

def passwordTooCommon(password):
    listChar = ['@', '*', '&', '%']
    digitFound = False
    letterFound = False
    specialFound = False
    for i in password:
        if i.isalpha():
            letterFound = True
        elif i.isdigit():
            digitFound = True
        elif i in listChar:
            specialFound = True
    if digitFound and not letterFound and not specialFound:
        return True
    elif letterFound and not digitFound and not specialFound:
        return True
    elif specialFound and not digitFound and not letterFound:
        return True
    else:
        return False
        
inputPassword = input()

while inputPassword != "Done":
    try:
        if not passwordLength(inputPassword):
            raise PasswordTooShortError("Password must contain at least 8 characters")
        if passwordTooCommon(inputPassword):
            raise PasswordTooCommonError("Password must be a combination of digits, letters, and special characters")
        if not passwordSpecialCharacter(inputPassword):
            raise PasswordNoSpecialCharactersError("Password must contain at least 1 special character")
        if passwordSpace(inputPassword):
            raise PasswordContainsSpacesError("Password must not contain empty spaces")
        print (f"Password is valid")

    except (PasswordTooShortError,
           PasswordTooCommonError,
           PasswordNoSpecialCharactersError,
           PasswordContainsSpacesError) as e:
        print (e)
        
    inputPassword = input()
