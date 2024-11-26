#Mirror Words

import re

words = input()

patternMirror = r"(?<=([\@\#]))([a-zA-Z]{3,})\1\1([a-zA-Z]{3,})(?=\1)"
mirrorMatches = re.findall(patternMirror, words)

mirrorWords = []

#print (mirrorMatches)
#print (len(mirrorMatches))

for i in mirrorMatches:
    word1 = i[1][::-1]
    word2 = i[2]
    if word1 == word2:
        combination = i[1] +" <=> "+ i[2]
        mirrorWords.append(combination)

if mirrorMatches:
    print (f"{len(mirrorMatches)} word pairs found!")
    if mirrorWords:
        print (f"The mirror words are:\n{', '.join(mirrorWords)}")
    else:
        print (f"No mirror words!")
else:
    print (f"No word pairs found!")
    print (f"No mirror words!")
    