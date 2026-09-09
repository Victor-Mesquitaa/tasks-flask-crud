class Task:
    def __init__(self, id, title, description, completed=False):
        self.id = id
        self.id = title
        self.id = description
        self.completed = completed

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed
        }