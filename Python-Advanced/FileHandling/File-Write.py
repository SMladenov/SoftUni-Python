#File Write

dirPath = "C:\\Users\\Strahil.Mladenov\\Desktop\\"

file = open(f"{dirPath}exampleWrite.txt", 'w')

file.write("This is the write command.\n")
file.write("Second Line\n")
file.close()

print (open(f"{dirPath}exampleWrite.txt", 'r').read())

file.close()

file = open(f"{dirPath}exampleWrite.txt", 'a')

file.write("This is the write command with append.\n")
file.write("Second Line with append")
file.close()

print (open(f"{dirPath}exampleWrite.txt", 'rt').read())

file.close()

#File Write 2

fullPath = "C:\\Users\\Strahil.Mladenov\\Desktop\\fileCreation2.txt"

with open(fullPath, 'x') as file:
    file.write("Something with this experiment")

print (open(fullPath, 'rt').read())