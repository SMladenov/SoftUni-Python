#Line Numbers

fullPath = "C:\\Users\\Strahil.Mladenov\\Desktop\\FileManipulation\\text.txt"
outputFile = "C:\\Users\\Strahil.Mladenov\\Desktop\\FileManipulation\\outputLineNumbers.txt"

listPunctuation = ['-', ',', '.', '!', '?', '\'', '"', '_']

with open(fullPath, 'rt') as file:
    listRead = [i.strip() for i in file.readlines() if i.strip()]
    counter = 0
    for line in listRead:
        counter += 1
        countPunc = 0
        countLetter = 0
        for char in line:
            if char.isalpha():
                countLetter += 1
            elif char in listPunctuation:
                countPunc += 1
        with open(outputFile, 'a') as output:
            output.write(f"Line {counter}: {line} ({countLetter})({countPunc})\n")

with open(outputFile, 'rt') as output:
    print (output.read())
