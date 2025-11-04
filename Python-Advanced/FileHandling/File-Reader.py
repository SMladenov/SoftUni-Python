#File Reader

import os

fileName = input()
dirPath = "C:\\Users\\Strahil.Mladenov\\Desktop\\"
fullPath = os.path.join(dirPath, fileName)
fileOpen = open(fullPath, 'r')

#print (fileOpen.read())

#Bytes of the file like a cursor and it stays there
#print (fileOpen.read(4))

#A List with each line as element
print (sum([int(i.strip()) for i in fileOpen.readlines() if i.strip()]))

