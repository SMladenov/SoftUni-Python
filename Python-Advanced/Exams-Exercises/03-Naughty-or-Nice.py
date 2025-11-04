#Naughty or Nice

def naughty_or_nice_list (listNames, *args, **kwargs):

    dicNiceness = {}

    niceList = []
    naughtyList = []
    notFoundList = []
    
    santaList = list(listNames)
    kidsArgs = args
    kidsDic = kwargs

    for kid in kidsArgs:
        kidNumber = int(kid.split('-')[0])
        kidNiceness = kid.split('-')[1]

        matches = [kid for kid in santaList if kid[0] == kidNumber]

        if len(matches) == 1:
            kid = matches[0]
            if kidNiceness == "Nice":
                niceList.append(kid[1])
            elif kidNiceness == "Naughty":
                naughtyList.append(kid[1])
            santaList.remove(kid)

    for name, niceness in kidsDic.items():
        matches = [kid for kid in santaList if kid[1] == name]

        if len(matches) == 1:
            kid = matches[0]
            if niceness == "Nice":
                niceList.append(kid[1])
            elif niceness == "Naughty":
                naughtyList.append(kid[1])
            santaList.remove(kid)

    notFoundList = [kid[1] for kid in santaList]

    listForOutput = []

    if niceList:
        listForOutput.append(f"Nice: {', '.join(niceList)}")
    if naughtyList:
        listForOutput.append(f"Naughty: {', '.join(naughtyList)}")
    if notFoundList:
        listForOutput.append(f"Not found: {', '.join(notFoundList)}")

    return '\n'.join(listForOutput)

print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))

print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
    ))

    
print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))
