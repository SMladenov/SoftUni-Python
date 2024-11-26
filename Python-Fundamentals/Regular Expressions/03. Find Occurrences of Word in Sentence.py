#Find Occurences of Word in Sentence

import re

sentence = input()
word = input()

#re.escape escapes any special characters in the input word to ensure 
#it is treated as a literal string
#The (' + <word> + r') group the word to be treated as a single unit and capture it in group
reg = r'\b(' + re.escape(word) + r')\b'
listMatch = re.findall(reg, sentence, re.IGNORECASE)

print (len(listMatch))
