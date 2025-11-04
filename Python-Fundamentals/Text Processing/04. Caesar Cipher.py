#Caesar Cipher

inputStr = input()

for i in inputStr:
    print (f"{chr(ord(i) + 3)}", end = "")