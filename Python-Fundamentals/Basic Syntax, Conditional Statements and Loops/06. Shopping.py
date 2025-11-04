budget = int(input())

cmd = input()

while cmd != "End":
    intParse = int(cmd)
    budget = budget - intParse
    if budget < 0:
        print (f"You went in overdraft!")
        break
    cmd = input()

if cmd == "End":
    print (f"You bought everything needed.")
    