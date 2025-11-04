#Articles

class Article:
    def __init__ (self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
    def edit (self, newContent):
        self.content = newContent
    def change_author (self, newAuthor):
        self.author = newAuthor
    def rename (self, newTitle):
        self.title = newTitle
    def __repr__ (self):
        return f"{self.title} - {self.content}: {self.author}"
    