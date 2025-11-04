from math import ceil

class PhotoAlbum:
    def __init__ (self, pages: int):
        self.pages = pages
        self.photos: list = []

        for _ in range(pages):
            self.photos.append([])
    
    @classmethod
    def from_photos_count (cls, photos_count: int):
        pagesNeeded = ceil(photos_count / 4)
        return cls(pagesNeeded)
        

    def add_photo(self, label: str):

        for row in range (0, len(self.photos)):
           if len(self.photos[row]) < 4:
               self.photos[row].append(label)
               return f"{label} photo added successfully on page {row + 1} slot {len(self.photos[row])}"
        return f"No more free slots"
    

    def display (self):
        
        listToOutput = []
        listToOutput.append("-" * 11)
        for row in range (0, len(self.photos)):
            if not self.photos[row]:
                listToOutput.append("")
            else:
                stringToBuild = "[] " * len(self.photos[row])
                listToOutput.append(stringToBuild.strip())
            listToOutput.append("-" * 11)

        return '\n'.join(listToOutput)


album = PhotoAlbum(1)
album.add_photo("baby")
album.add_photo("first grade")
album.add_photo("eight grade")
album.add_photo("party with friends")
result = album.display().strip()
print(result)