#Movie Organizer

def movie_organizer (*args):

    dicGenres = {}

    for name, genre in args:
        if genre not in dicGenres.keys():
            dicGenres[genre] = [name]
        else:
            dicGenres[genre].append(name)

    dicGenresSorted = dict(sorted(dicGenres.items(), key= lambda x: (-len(x[1]), x[0])))

    listToOutput = []
    
    for genre, groupGenre in dicGenresSorted.items():
        listToOutput.append(f"{genre} - {len(groupGenre)}")
        groupGenre.sort()
        for movie in groupGenre:
            listToOutput.append(f"* {movie}")

    return '\n'.join(listToOutput)

# print(movie_organizer(
#     ("The Matrix", "Sci-fi")))

# print(movie_organizer(
#     ("The Godfather", "Drama"),
#     ("The Hangover", "Comedy"),
#     ("The Shawshank Redemption", "Drama"),
#     ("The Pursuit of Happiness", "Drama"),
#     ("The Hangover Part II", "Comedy")))

print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))
