#Repeat Text

import re

class CustomException(Exception):
    pass

def is_int(randomString):
    pattern = r"^[0-9]+$"
    return bool(re.findall(pattern, randomString))

textToRepeat = input()

try:
    timesToRepeat = input()
    if not is_int(timesToRepeat):
        raise CustomException("Variable times must be an int")

    timesToRepeat = int(timesToRepeat)
    print(f"{textToRepeat * timesToRepeat}")
except CustomException as e:
    print(e)
