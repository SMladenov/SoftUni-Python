#Extract Emails

import re

randomStr = input()
pattern = r"\b(?<=\s)[A-Za-z0-9]+(?:[._-][A-Za-z0-9]+)*\@[a-zA-Z]+(?:[-][a-zA-Z]+)*\.[a-zA-Z.]+\b"

listMatch = re.findall(pattern, randomStr)

if listMatch:
    for i in listMatch:
        print (i)
        