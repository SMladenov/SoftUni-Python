#Balanced Parantheses
#Stack

inputRandomStr = input()

listOpened = ['(', '{', '[']
listClosed = [')', '}', ']']
listBoth = ['()', '{}', '[]']

stackOpened = []
isBalanced = True

for i in inputRandomStr:
    if i in listOpened:
        stackOpened.append(i)
    elif i in listClosed:
        if stackOpened and f"{stackOpened[-1]}{i}" in listBoth:
            stackOpened.pop()
        else:
            print (f"NO")
            isBalanced = False
            break

if isBalanced:
    if not stackOpened:
        print (f"YES")
    else:
        print (f"NO")
