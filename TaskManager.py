import Task

class TaskManager:
    tasks = []

    def addTask(self, task):
        if isinstance(task, Task.Task):
            self.tasks.append(task)
            return f"ADDED TASK: {task.__str__()}"

        else:
            return "Wrong type of Task"

    def removeTask(self, task):
        try:
            self.tasks.remove(task)
            return f"REMOVE TASK: {task.__str__()}"
        except:
            return "Task not found"

    def CheckMarkTask(self, task, id):
        if task.id == id:
            task.complete()
            return f"TASK COMPLETED: {task.__str__()}"
        else:
            return "Wrong input id"

    def ListTasks(self):
        for task in self.tasks:
            print(task.__str__())