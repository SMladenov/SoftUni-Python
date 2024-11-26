#Extract the Links

import re
import sys

pattern = r"\bw{3}\.[a-zA-Z0-9]+(?:[-.][a-zA-Z0-9]+)*\.[a-zA-Z]+\b"

inputStr = sys.stdin.read()
#inputStr = input()

tryMatches = re.findall(pattern, inputStr)

print ('\n'.join(tryMatches))
