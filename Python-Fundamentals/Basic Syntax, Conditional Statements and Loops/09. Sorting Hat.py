#Sorting Hat

name = input()

def toWhichUniversity(length):
    dicUniversities = {length < 5: "Gryffindor", length == 5: "Slytherin", length == 6: "Ravenclaw", length > 6: "Hufflepuff"}
    return dicUniversities.get(True)

while name != "Welcome!":
    if name == "Voldemort":
        print (f"You must not speak of that name!")
        break
    university = toWhichUniversity(len(name))
    print (f"{name} goes to {university}.")
    name = input()
if name == "Welcome!":
    print (f"Welcome to Hogwarts.")
