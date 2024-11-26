#Decipher This!

words = input().split(' ')

listWords = []

for word in words:
    finalString = ""
    decValue = ""
    for i in word:
        if i.isdigit():
            decValue += i
        else:
            break
    lenAfterDec = word[len(decValue):]
    if len(lenAfterDec) >= 2:
        finalString = chr(int(decValue)) + word[len(word) - 1] + word[len(decValue) + 1:len(word) - 1] + word[len(decValue)]
        listWords.append(finalString)
    elif len(lenAfterDec) < 2:
        finalString = chr(int(decValue)) + word[len(decValue):]
        listWords.append(finalString)

print (f"{' '.join(listWords)}")
