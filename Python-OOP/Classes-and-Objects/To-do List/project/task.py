
class Task:
    def __init__ (self, name: str, due_date: str):
        self.name = name
        self.due_date = due_date
        self.comments: list = []
        self.completed: bool = False
    
    def change_name (self, new_name: str):
        if new_name == self.name:
            return f"Name cannot be the same."
        else:
            self.name = new_name
            return f"{self.name}"
    
    def change_due_date (self, new_date: str):
        if new_date == self.due_date:
            return f"Date cannot be the same."
        else:
            self.due_date = new_date
            return f"{self.due_date}"
    
    def add_comment (self, comment: str):
        self.comments.append(comment)
    
    def edit_comment(self, comment_number: int, new_comment: str):
        if comment_number < 0 or comment_number >= len(self.comments):
            return f"Cannot find comment."
        else:
            self.comments[comment_number] = new_comment
            return f"{', '.join(self.comments)}"
    
    def details (self):
        return f"Name: {self.name} - Due Date: {self.due_date}"

    