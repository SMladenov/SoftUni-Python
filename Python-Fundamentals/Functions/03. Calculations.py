#Calculations

def calculations(action, num1, num2):
    if action == "multiply":
        return num1 * num2
    elif action == "divide":
        return num1 // num2
    elif action == "add":
        return num1 + num2
    elif action == "subtract":
        return num1 - num2

action = input()
num1 = int(input())
num2 = int(input())

print (f"{calculations(action, num1, num2)}")
