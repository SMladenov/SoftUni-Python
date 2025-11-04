#Match Full Name

import re

names = input()
regex = r'\b[A-Z][a-z]+\ [A-Z][a-z]+\b'
matches = re.findall(regex, names)
print (f"{' '.join(matches)}")