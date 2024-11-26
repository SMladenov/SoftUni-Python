#Extract File

filePath = input().split('\\')
fileNameExtension = filePath[len(filePath) - 1].split('.')

print (f"File name: {fileNameExtension[0]}\nFile extension: {fileNameExtension[1]}")