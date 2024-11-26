#Company Users

cmd = input()

dicCompanies = {}

while cmd != "End":
    cmdSplit = cmd.split(' -> ')
    company = cmdSplit[0]
    employeeId = cmdSplit[1]
    if company not in dicCompanies.keys():
        dicCompanies[company] = []
        dicCompanies[company].append(employeeId)
    else:
        if employeeId not in dicCompanies[company]:
            dicCompanies[company].append(employeeId)
    cmd = input()

for key, value in dicCompanies.items():
    print (f"{key}")
    print ('\n'.join(f"-- {i}" for i in value))