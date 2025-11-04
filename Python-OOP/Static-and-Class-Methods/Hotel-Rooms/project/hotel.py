from project.room import Room

class Hotel:
    def __init__ (self, name: str):
        self.name = name
        self.rooms: list[Room] = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")
    
    def add_room(self, room: Room):
        self.rooms.append(room)
    
    def take_room(self, room_number, people):
        roomList = [room for room in self.rooms if room.number == room_number]

        if roomList:
            result = roomList[0].take_room(people)
            if result is None:
                self.guests += people
            else:
                return result
    
    def free_room (self, room_number):
        roomList = [room for room in self.rooms if room.number == room_number]

        if roomList:
            room = roomList[0]
            currentGuests = room.guests
            result = room.free_room()
            if result is None:
                self.guests -= currentGuests
            else:
                return result
            
    
    def status(self):
        freeRooms = [room.number for room in self.rooms if not room.is_taken]
        takenRooms = [room.number for room in self.rooms if room.is_taken]
    
        listToOutput = []
        listToOutput.append(f"Hotel {self.name} has {self.guests} total guests")
        listToOutput.append(f"Free rooms: {', '.join(map(str, freeRooms))}")
        listToOutput.append(f"Taken rooms: {', '.join(map(str, takenRooms))}")

        return '\n'.join(listToOutput)
