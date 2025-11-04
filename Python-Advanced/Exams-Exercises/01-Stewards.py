#Stewards

seats = input().split(', ')
dicSeats = {seat: "not taken" for seat in seats}

firstSeq = [int(i) for i in input().split(', ')]
secondSeq = [int(i) for i in input().split(', ')]

seatMatches = []
rotations = 0

while len(seatMatches) < 3 and rotations < 10:
    rotations += 1
    currentFirstSeq = firstSeq[0]
    currentSecondSeq = secondSeq[-1]
    asciiChar = chr(currentFirstSeq + currentSecondSeq)

    combinedSeat1 = str(currentFirstSeq) + asciiChar
    combinedSeat2 = str(currentSecondSeq) + asciiChar

    if combinedSeat1 in seats or combinedSeat2 in seats:
        firstSeq.pop(0)
        secondSeq.pop()
        if combinedSeat1 in dicSeats.keys():
            if dicSeats[combinedSeat1] == "not taken":
                seatMatches.append(combinedSeat1)
                dicSeats[combinedSeat1] = "taken"
        else:
            if dicSeats[combinedSeat2] == "not taken":
                seatMatches.append(combinedSeat2)
                dicSeats[combinedSeat2] = "taken"
    else:
        firstSeq.pop(0)
        secondSeq.pop()
        firstSeq.append(currentFirstSeq)
        secondSeq.insert(0, currentSecondSeq)

print (f"Seat matches: {', '.join(seatMatches)}")
print (f"Rotations count: {rotations}")
