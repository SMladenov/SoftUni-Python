#Tic-Tac-Toe

first = input().split(' ')
second = input().split(' ')
third = input().split(' ')

winner = False
whoIsTheWinner = ""

for i in range (0, len(first)):
    if i == 0:
        if (first[i] == first[i + 1] == first[i + 2]) and first[i] != '0':
            winner = True
            whoIsTheWinner = first[i]
            break
    for b in range (0, len(second)):
        if b == 0:
            if (second[b] == second[b + 1] == second[b + 2]) and second[b] != '0':
                winner = True
                whoIsTheWinner = second[b]
                break
        for c in range (0, len(third)):
            if c == 0:
                if (third[c] == third[c + 1] == third[c + 2]) and third[c] != '0':
                    winner = True
                    whoIsTheWinner = third[c]
                    break
            if (first[i] == second[i] == third[i]) and first[i] != '0':
                winner = True
                whoIsTheWinner = first[i]
                break
            if (i == 0 and b == 1 and c == 2) or (i == 2 and b == 1 and c == 0):
                if (first[i] == second[b] == third[c]):
                    winner = True
                    whoIsTheWinner = third[c]
                    break
                    
        if winner:
            break
    if winner:
        break

if whoIsTheWinner == "1":
    print (f"First player won")
elif whoIsTheWinner == "2":
    print (f"Second player won")
elif whoIsTheWinner == "" or whoIsTheWinner == "0":
    print (f"Draw!")
    