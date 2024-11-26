#Password Validator

def validator (password):
    result = ""
    digitCounter = 0
    if not 6 <= len(password) <= 10:
        result += "Password must be between 6 and 10 characters$"
    for i in password:
        if not i.isalpha() and not i.isdigit():
            result += "Password must consist only of letters and digits$"
            break
    for i in password:
        if i.isdigit():
            digitCounter += 1
    if digitCounter < 2:
        result += "Password must have at least 2 digits$"
    return result
            
password = input()

result = validator(password)
if result != "":
    result = result.split('$')
    result = [i for i in result if i.strip()]
    for i in result:
        print (i)
else:
    print (f"Password is valid")