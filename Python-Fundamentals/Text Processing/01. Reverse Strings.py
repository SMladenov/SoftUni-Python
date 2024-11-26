#Reverse Strings

cmd = input()

#while cmd != "end":
#    reverseCmd = ""
#    for i in range (len(cmd) - 1, -1, -1):
#        reverseCmd += cmd[i]
#    print (f"{cmd} = {reverseCmd}")
#    cmd = input()

while cmd != "end":
    reverseCmd = ""
    for i in reversed(cmd):
        reverseCmd += i
    print (f"{cmd} = {reverseCmd}")
    cmd = input()