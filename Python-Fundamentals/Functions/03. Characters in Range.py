#Characters in Range

def charsBetween(char1, char2):
    listChars = []
    dec1 = ord(char1)
    dec2 = ord(char2)
    for i in range (dec1 + 1, dec2):
        listChars.append(chr(i))
    return listChars

char1 = input()
char2 = input()

print (" ".join(charsBetween(char1, char2)))
