#Movie

class Movie:
    __watched_movies = 0
    def __init__ (self, name, director):
        self.name = name
        self.director = director
        self.watched = False
    def change_name (self, newName):
        self.name = newName
    def change_director (self, newDirector):
        self.director = newDirector
    def watch (self):
        if self.watched == False:
            self.watched = True
            Movie.__watched_movies += 1
    def __repr__ (self):
        return f"Movie name: {self.name}; Movie director: {self.director}. Total watched movies: {Movie.__watched_movies}"
    