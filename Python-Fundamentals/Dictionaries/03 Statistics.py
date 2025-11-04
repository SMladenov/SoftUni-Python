#Statistics

cmd = input()
dict = {}

while cmd != "statistics":
    cmdSplit = cmd.split(': ')
    key = cmdSplit[0]
    value = int(cmdSplit[1])
    if key not in dict.keys():
        dict[key] = value
    else:
        dict[key] += value
    cmd = input()

totalItems = 0
totalValue = 0

print (f"Products in stock:")
for key, value in dict.items():
    print (f"- {key}: {value}")
    totalItems += 1
    totalValue += dict[key]

print (f"Total Products: {totalItems}\nTotal Quantity: {totalValue}")