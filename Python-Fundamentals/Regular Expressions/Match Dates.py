#Match Dates

import re

dates = input()
#pattern = r'\b(?P<day>\d{2})([-./])(?P<month>[A-Z][a-z]{2})\2(?P<year>\d{4})\b'
pattern = r'\b(\d{2})([-./])([A-Z][a-z]{2})\2(\d{4})\b'
matchs = re.findall(pattern, dates)

for item in matchs:
    print (f"Day: {item[0]}, Month: {item[2]}, Year: {item[3]}")