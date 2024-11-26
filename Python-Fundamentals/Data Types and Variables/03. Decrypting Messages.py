#Decrypting Messages

finalString = ""

key = int(input())
num = int(input())

for i in range (num):
    char1 = input()
    finalString += chr(key + ord(char1))

print (f"{finalString}")
