#Data Types

def tryType(type, input1):
    if type == "int":
        return int(input1) * 2
    elif type == "real":
        return f"{(float(input1) * 1.5):.2f}"
    elif type == "string":
        return f"${input1}$"

type = input()
input1 = input()

print (f"{tryType(type, input1)}")