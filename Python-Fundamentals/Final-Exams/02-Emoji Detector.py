#Emoji Detector

import re

inputMsg = input()

coolness = 1

for i in inputMsg:
    if i.isdigit():
        coolness *= int(i)

patternEmoji = r"(\*{2}|\:{2})([A-Z][a-z]{2,})\1"
emojiMatches = re.findall(patternEmoji, inputMsg)

print (f"Cool threshold: {coolness}\n{len(emojiMatches)} emojis found in the text. The cool ones are:")

for i in emojiMatches:
    tempAmount = 0
    for b in i[1]:
        tempAmount += ord(b)
    if tempAmount >= coolness:
        print (f"{i[0]}{i[1]}{i[0]}")