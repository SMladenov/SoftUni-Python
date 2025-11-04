#Word Count

import re
import os

fullPath1 = "C:\\Users\\Strahil.Mladenov\\Desktop\\FileManipulation\\file1.txt"
fullPath2 = "C:\\Users\\Strahil.Mladenov\\Desktop\\FileManipulation\\file2.txt"

dicWords = {}

with open(fullPath1, 'rt') as file1:
    with open(fullPath2, 'rt') as file2:
        file1Read = file1.read().split()
        file2Read = file2.read().lower()

        for word in file1Read:
            if word.lower() in file2Read:
                #patternMatch = fr"\b{re.escape(word)}\b"
                patternMatch = fr"\b{word}\b"
                #countMatches = len(re.findall(patternMatch, file2Read, re.IGNORECASE))
                countMatches = len(re.findall(patternMatch, file2Read))
                if word not in dicWords.items():
                    dicWords[word] = countMatches

sortedDic = dict(sorted(dicWords.items(), key=lambda x: -x[1]))

fullPath3 = "C:\\Users\\Strahil.Mladenov\\Desktop\\FileManipulation\\file_output.txt"
with open(fullPath3, 'a') as fileOutput:
    for key, value in sortedDic.items():
        fileOutput.write(f"{key} - {value}\n")

print (open(fullPath3, 'rt').read())

print (sortedDic)

print (fileOutput.closed)
print (file1.closed)
print (file2.closed)
