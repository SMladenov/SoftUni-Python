#Rage Quit

strInput = input()

updated = ""

index = 0

tempNum = ""
tempStr = ""
while index < len(strInput):
    if not strInput[index].isdigit():
        while index < len(strInput) and not strInput[index].isdigit():
            tempStr += strInput[index]
            index += 1
    if strInput[index].isdigit():
        while index < len(strInput) and strInput[index].isdigit():
            tempNum += strInput[index]
            index += 1
        updated += (tempStr * int(tempNum)).upper()
        tempNum = ""
        tempStr = ""

uniqueSymbols = []
for i in updated:
    if i not in uniqueSymbols:
        uniqueSymbols.append(i)

print (f"Unique symbols used: {len(uniqueSymbols)}\n{updated}")