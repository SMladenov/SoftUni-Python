#Comment

class Comment:
    def __init__(self, username, content, likes = 0):
        self.username = username
        self.content = content
        self.likes = likes

comment = Comment("Pesho", "TestTest", 2)
print (f"{comment.username}\n{comment.content}\n{comment.likes}")