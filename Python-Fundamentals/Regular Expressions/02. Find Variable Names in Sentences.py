#Find Variable Names in Sentences

import re

strExample = input()

reg = r'\b\_[a-zA-Z0-9]+(?=\s|$)'
listMatch = re.findall(reg, strExample)

for index, i in enumerate(listMatch):
    if index < len(listMatch) - 1:
        print (f"{i[1:]}", end = ",")
    else:
        print (f"{i[1:]}")
        