class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        task_number = len(self.tasks) + 1
        self.tasks.append(f"{task_number}. {task}")
        print("Task added successfully")

    def remove_task(self, task_number):
        if task_number > 0 and task_number <= len(self.tasks):
            del self.tasks[task_number - 1]
            print("You've done it Task removed successfully!")
        else:
            print("Oops,Task not found.")

    def view_tasks(self):
        if self.tasks:
            print("Hey , here's your To-Do List:")
            for task in self.tasks:
                print(task)
        else:
            print("Hey your To-Do List is empty. Why not add some tasks?")

    def update_task(self, task_number, new_task):
        if task_number > 0 and task_number <= len(self.tasks):
            self.tasks[task_number - 1] = f"{task_number}. {new_task}"
            print("Got it Task updated successfully!")
        else:
            print("Oops,  Task not found.")

def main():
    todo_list = ToDoList()

    print("Hey  Welcome to your To-Do List app.")

    while True:
        print("\nWhat do you want to do?")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Update Task")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            task = input("What task would you like to add ? ")
            todo_list.add_task(task)
        elif choice == '2':
            task_number = int(input("Which task number have you completed ? "))
            todo_list.remove_task(task_number)
        elif choice == '3':
            todo_list.view_tasks()
        elif choice == '4':
            task_number = int(input("Enter the task number you want to update ? "))
            new_task = input("What's the new task ? ")
            todo_list.update_task(task_number, new_task)
        elif choice == '5':
            print("Goodbye See you later.")
            break
        else:
            print("Oops! Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
