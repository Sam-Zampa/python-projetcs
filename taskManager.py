"""
Task Manager
---
code made in October 2023
"""
class Task:
    def __init__(self, title, description, date, status):
        self.title = title
        self.description = description
        self.date = date
        self.status = status

class TaskManager:
    def __init__(self):
        self.tasks = []

    # 1 Add
    def add_task(self, title, description, date, status):
        for task in self.tasks:
            if task.title.lower() == title.lower():
                while True:
                    new_title = input(f"A task with the title '{title}' already exists. Please enter a different title: ")
                    print("")
                    if not any(task.title.lower() == new_title.lower() for task in self.tasks):
                        title = new_title
                        break
        task = Task(title, description, date, status)
        self.tasks.append(task)
        print("")
        print(f"Task with title '{title}' added successfully!")
        print("")

    # 2 List
    def list_tasks(self):
        for task in self.tasks:
            print(f"#{task.title}#\n{task.description}\n{task.date}\n{task.status}\n")

    # 3 Complete
    def mark_completed(self, title):
        for task in self.tasks:
            if task.title.lower() == title.lower():
                task.status = "Completed!"
                print(f"Congratulations! The task with title '{title}' has been completed!")
                print("")
                return
        print(f"Task with title '{title}' not found.")
        print("")

    # 4 Rename and Redescribe
    def edit(self, title, new_title, new_description):
        for task in self.tasks:
            if task.title.lower() == title.lower():
                task.title = new_title
                task.description = new_description
                print("Task title and description updated!")
                print("")
                return
        print(f"Task with title '{title}' not found.")
        print("")

    # 5 Delete
    def delete_task(self, title):
        for task in self.tasks:
            if task.title.lower() == title.lower():
                self.tasks.remove(task)
                print(f"Task with title '{title}' deleted successfully!")
                print("")
                return
        print(f"Task with title '{title}' not found.")
        print("")

    # 6 Export
    def export_tasks(self, filename):
        with open(filename, "w") as file:
            for task in self.tasks:
                file.write(f"#{task.title}#\n{task.description}\n{task.date}\n{task.status}\n")

if __name__ == "__main__":
    manager = TaskManager()

    while True:
        print("- Tasks -")
        print("\nOptions:")
        print("1 - Add task")
        print("2 - List tasks")
        print("3 - Mark task as completed")
        print("4 - Edit task title and description")
        print("5 - Delete task")
        print("6 - Export task list")
        print("7 - Exit")
        print("")

        option = input("Choose an option: ")
        print("")

        if option == "1":
            title = input("Title: ")
            description = input("Description: ")
            date = input("Date: ")
            status = "In progress"
            manager.add_task(title, description, date, status)
        elif option == "2":
            manager.list_tasks()
        elif option == "3":
            title = input("Title of the task you want to mark as completed: ")
            manager.mark_completed(title)
        elif option == "4":
            title = input("Title of the task you want to edit: ")
            new_title = input("Enter the new title: ")
            new_description = input("Enter the new description: ")
            manager.edit(title, new_title, new_description)
        elif option == "5":
            title = input("Title of the task you want to delete: ")
            manager.delete_task(title)
        elif option == "6":
            filename = input("Enter the filename to export tasks: ")
            manager.export_tasks(filename)
        elif option == "7":
            break
