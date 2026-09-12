class Task:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description
        self.completed = False

    def complete(self):
        self.completed = True
        return self

    def __repr__(self):
        return f"Task id: {self.id}, name: {self.name}, description: {self.description}, completed: {self.completed}"

    def __str__(self):
        return self.__repr__()


