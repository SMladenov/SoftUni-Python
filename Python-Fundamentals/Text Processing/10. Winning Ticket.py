#Winning Ticket

def is_valid (ticket):
    validSymbols = ['@', '#', '$', '^']
    indexLeft = 0
    indexRight = 19
    validLeft = 0
    validLeftSymbol = ""
    validRight = 0
    validRightSymbol = ""
    
    if len(ticket) != 20:
        return f"invalid ticket"

    while indexLeft < 10:
        if ticket[indexLeft] in validSymbols:
            validLeft += 1
            validLeftSymbol = ticket[indexLeft]
            while indexLeft < 9 and ticket[indexLeft] == ticket[indexLeft + 1]:
                validLeft += 1
                indexLeft += 1
        if validLeft < 6:
            validLeft = 0
            validLeftSymbol = ""
        indexLeft += 1

    while indexRight > 9:
        if ticket[indexRight] in validSymbols:
            validRight += 1
            validRightSymbol = ticket[indexRight]
            while indexRight > 10 and ticket[indexRight] == ticket[indexRight - 1]:
                validRight += 1
                indexRight -= 1
        if validRight < 6:
            validRight = 0
            validRightSymbol = ""
        indexRight -= 1

    if (10 > validLeft > 5)  and (10 > validRight > 5): #and (validLeftSymbol == validRightSymbol):
        if validLeft <= validRight:
            return f'ticket "{ticket}" - {validLeft}{validLeftSymbol}'
        if validRight < validLeft:
            return f'ticket "{ticket}" - {validRight}{validRightSymbol}'
    if (validLeft == 10 and validRight == 10) and (validLeftSymbol == validRightSymbol):
        return f'ticket "{ticket}" - {validLeft}{validLeftSymbol} Jackpot!'
    if validLeft < 6 or validRight < 6:
        return f'ticket "{ticket}" - no match'

tickets = input().split(', ')
tickets = [i.strip() for i in tickets if i.strip()]

for i in tickets:
    print (f"{is_valid(i)}")