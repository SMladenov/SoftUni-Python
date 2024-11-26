#Match Phone Number

import re
#pattern = '\\b\+359([ -])2\1\d{3}\1\d{4}\\b'
pattern = "(\+359-2-[0-9]{3}-[0-9]{4}\\b|\+359 2 [0-9]{3} [0-9]{4})\\b"
text = input()
matches = re.findall(pattern, text)
print (f"{', '.join(matches)}")