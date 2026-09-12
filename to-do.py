import Task
import TaskManager

if __name__ == '__main__':
    task1 = Task.Task(1, "Java exercise", "Test of Java knowledge")
    task2 = Task.Task(2, "Python exercise", "Test for Python knowledge")
    manager = TaskManager.TaskManager()

    manager.addTask(task1)
    manager.addTask(task2)
    manager.ListTasks()

    manager.CheckMarkTask(task1, 1)
    manager.CheckMarkTask(task2, 3)
    manager.ListTasks()

    manager.removeTask(task1)
    manager.ListTasks()

