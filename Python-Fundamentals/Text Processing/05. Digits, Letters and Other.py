#Digits, Letters, and Other

inputStr = input()
letters = ""
digits = ""
other = ""

for i in inputStr:
    if i.isdigit():
        digits += i
    elif i.isalpha():
        letters += i
    else:
        other += i

print (f"{digits}\n{letters}\n{other}")