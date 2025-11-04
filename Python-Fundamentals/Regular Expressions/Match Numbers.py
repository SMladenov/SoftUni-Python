#Match Numbers

import re

inputNumbers = input()

patternNumbers = r"(?:^|(?<=\s))\-?(?:0|[1-9][0-9]*)(?:\.\d+)?(?:$|(?=\s))"

matchesNumbers = re.findall(patternNumbers, inputNumbers)

print (f"{' '.join(matchesNumbers)}")