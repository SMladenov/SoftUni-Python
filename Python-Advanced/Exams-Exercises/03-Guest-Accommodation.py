#Guest Accommodation

def accommodate(*args, **kwargs):
    dicRoomsSorted = dict(sorted(kwargs.items(), key= lambda x: (x[1], x[0])))
    guestsNumbers = args

    dicSucessfull = {}
    sucessfullAccommodations = 0
    
    for guests in guestsNumbers:
        for room, capacity in dicRoomsSorted.items():
            if capacity == guests:
                dicSucessfull[room] = guests
                del dicRoomsSorted[room]
                sucessfullAccommodations += guests
                break
            elif capacity > guests:
                dicSucessfull[room] = guests
                del dicRoomsSorted[room]
                sucessfullAccommodations += guests
                break
                
    if dicSucessfull:
        dicSucessSorted = dict(sorted(dicSucessfull.items(), key= lambda x: x[0]))

    listOutput = []

    if dicSucessfull:
        listOutput.append(f"A total of {len(dicSucessSorted)} accommodations were completed!")
        for room, guests in dicSucessSorted.items():
            roomNumber = room.split('_')[1]
            listOutput.append(f"<Room {roomNumber} accommodates {guests} guests>")
    else:
        listOutput.append(f"No accommodations were completed!")

    if sucessfullAccommodations < sum(guestsNumbers):
        listOutput.append(f"Guests with no accommodation: {sum(guestsNumbers) - sucessfullAccommodations}")
    if dicRoomsSorted:
        listOutput.append(f"Empty rooms: {len(dicRoomsSorted)}")

    return '\n'.join(listOutput)

print(accommodate(5, 4, 2, room_305=6, room_410=5, room_204=2))

#print(accommodate(10, 9, 8, room_307=6, room_802=5))

#print(accommodate(1, 2, 4, 8, room_102=3, room_101=1, room_103=2))
