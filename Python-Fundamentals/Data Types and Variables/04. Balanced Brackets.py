#Balanced Brackets

num = int(input())

opened = 0
isBalanced = True
finalBalanced = True

for i in range (num):
    randomStr = input().strip()
    if randomStr == "(":
        opened += 1
        if opened > 1:
            finalBalanced = False
    if randomStr == ")":
        opened -= 1
        if opened < 0:
            finalBalanced = False

if opened != 0:
    isBalanced = False

if finalBalanced == False:
    isBalanced = False

if isBalanced:
    print (f"BALANCED")
else:
    print (f"UNBALANCED")