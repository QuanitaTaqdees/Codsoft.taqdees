class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        if self.tasks:
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")
        else:
            print("No tasks yet!")

    def complete_task(self, index):
        try:
            del self.tasks[index - 1]
            print("Task completed!")
        except IndexError:
            print("Invalid task index")

    def delete_task(self, index):
        try:
            del self.tasks[index - 1]
            print("Task deleted!")
        except IndexError:
            print("Invalid task index")

    def update_task(self, index, new_task):
        try:
            self.tasks[index - 1] = new_task
            print("Task updated!")
        except IndexError:
            print("Invalid task index")


def main():
    todo_list = TodoList()
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Update Task")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            index = int(input("Enter task index to complete: "))
            todo_list.complete_task(index)
        elif choice == '4':
            index = int(input("Enter task index to delete: "))
            todo_list.delete_task(index)
        elif choice == '5':
            index = int(input("Enter task index to update: "))
            new_task = input("Enter new task: ")
            todo_list.update_task(index, new_task)
        elif choice == '6':
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
