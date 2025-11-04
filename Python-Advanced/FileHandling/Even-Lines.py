#Even Lines

fullPath = "C:\\Users\\Strahil.Mladenov\\Desktop\\FileManipulation\\text.txt"

listSpecialChars = ['-', ',', '.', '!', '?']

with open(fullPath, 'rt') as file:
    listRead = [i.strip() for i in file.readlines() if i.strip()]
    counter = 0
    for line in listRead:
        if counter % 2 == 0:
            for char in listSpecialChars:
                line = line.replace(char, '@')
            line = line.split()
            line.reverse()
            print (f"{' '.join(line)}")
        counter += 1
