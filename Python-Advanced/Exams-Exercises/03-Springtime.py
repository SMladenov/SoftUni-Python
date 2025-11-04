#Springtime

def start_spring (**kwargs):
    dicType = {}

    for springObject, type in kwargs.items():
        if type not in dicType.keys():
            dicType[type] = [springObject]
        else:
            dicType[type].append(springObject)

    dicTypeSorted = dict(sorted(dicType.items(), key=lambda x: (-len(x[1]), x[0])))

    listToOutput = []

    for type, listOfSpring in dicTypeSorted.items():
        listOfSpring.sort()
        listToOutput.append(f"{type}:")
        for springObject in listOfSpring:
            listToOutput.append(f"-{springObject}")

    return '\n'.join(listToOutput)

# example_objects = {"Water Lilly": "flower",
#                    "Swifts": "bird",
#                    "Callery Pear": "tree",
#                    "Swallows": "bird",
#                    "Dahlia": "flower",
#                    "Tulip": "flower",}
# print(start_spring(**example_objects))

# example_objects = {"Swallow": "bird",
#                    "Thrushes": "bird",
#                    "Woodpeckers": "bird",
#                    "Swallows": "bird",
#                    "Warblers": "bird",
#                    "Shrikes": "bird",}
# print(start_spring(**example_objects))

example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))
