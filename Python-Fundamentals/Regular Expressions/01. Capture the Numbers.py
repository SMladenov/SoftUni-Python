#Capture the Numbers

import re
import sys

strInput = sys.stdin.read()
regex = r'\d+'
matches = re.findall(regex, strInput, re.MULTILINE)

print (' '.join(matches))
