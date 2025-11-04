from project.album import Album
from project.song import Song

class Band:
    def __init__ (self, name: str):
        self.name = name
        self.albums: list[Album] = []
    
    def add_album (self, album: Album):
        if album not in self.albums:
            self.albums.append(album)
            return f"Band {self.name} has added their newest album {album.name}."
        else:
            return f"Band {self.name} already has {album.name} in their library."
        
    def remove_album (self, album_name: str):
        found = False
        for album in self.albums:
            if album.name == album_name:
                if album.published:
                    found = True
                    return f"Album has been published. It cannot be removed."
                else:
                    self.albums.remove(album)
                    found = True
                    return f"Album {album.name} has been removed."
                
        if not found:
            return f"Album {album_name} is not found."

    def details (self):
        listToOutput = []
        listToOutput.append(f"Band {self.name}")
        for album in self.albums:
            listToOutput.append(album.details())
        
        return '\n'.join(listToOutput)

# song = Song("Running in the 90s", 3.45, False)

# print(song.get_info())

# album = Album("Initial D", song)

# second_song = Song("Around the World", 2.34,

# False)

# print(album.add_song(second_song))

# print(album.details())

# print(album.publish())

# band = Band("Manuel")

# print(band.add_album(album))

# print(band.remove_album("Initial D"))

# print(band.details())