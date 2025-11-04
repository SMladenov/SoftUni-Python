#File Opener

import os

fileName = input()
dirPath = "C:\\Users\\Strahil.Mladenov\\Desktop\\"

try:
    fullPath = os.path.isfile(f"{dirPath}{fileName}")
    if fullPath:
        print (f"File Found")
    else:
        raise FileNotFoundError(f"File not Found")
except FileNotFoundError as e:
    print (e)


file = open("C:\\Users\\Strahil.Mladenov\\Desktop\\example.txt.txt", 'r')

print (file.read())

file.close()

