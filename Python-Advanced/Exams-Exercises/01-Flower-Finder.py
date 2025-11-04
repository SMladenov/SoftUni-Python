#Flower Finder

vowels = [i for i in input().split()]
consonants = [i for i in input().split()]

words = ["rose", "tulip", "lotus", "daffodil"]

wordFoundList = ["rose", "tulip", "lotus", "daffodil"]
wordFound = ""
wordIsFound = False

while vowels and consonants:
    currentVowel = vowels[0]
    currentConsonant = consonants[-1]

    for index, word in enumerate(words):

        if currentVowel in word:
            word = word.replace(currentVowel, "")
            if word == "":
                wordFound = wordFoundList[index]
                wordIsFound = True
                break
            words[index] = word

        if currentConsonant in word:
            word = word.replace(currentConsonant, "")
            if word == "":
                wordFound = wordFoundList[index]
                wordIsFound = True
                break
            words[index] = word
    
    vowels.pop(0)
    consonants.pop(-1)
    
    if wordIsFound:
        break

if wordIsFound:
    print (f"Word found: {wordFound}")
else:
    print (f"Cannot find any word!")

if vowels:
    print (f"Vowels left: {' '.join(vowels)}")
if consonants:
    print (f"Consonants left: {' '.join(consonants)}")
