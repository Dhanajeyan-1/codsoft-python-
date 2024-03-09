def display_todo_list(todo_list):
    print("To-Do List:")
    if not todo_list:
        print("No tasks in the list.")
    else:
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")
def add_task(todo_list):
    task = input("Enter the task: ")
    todo_list.append(task)
    print(f"Task '{task}' added to the list.")
def finish_task(todo_list, finished_tasks):
    display_todo_list(todo_list)
    if not todo_list:
        return
    try:
        index = int(input("Enter the task number to mark as finished: ")) - 1
        if 0 <= index < len(todo_list):
            finished_task = todo_list.pop(index)
            finished_tasks.append(finished_task)
            print(f"Task '{finished_task}' marked as finished.")
        else:
            print("Invalid task number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
def display_finished_tasks(finished_tasks):
    print("\nFinished Tasks:")
    if not finished_tasks:
        print("No tasks finished yet.")
    else:
        for index, task in enumerate(finished_tasks, start=1):
            print(f"{index}. {task}")
def main():
    todo_list = []
    finished_tasks = []
    while True:
        print("\nMenu:\n1. Add Task\n2. Finish Task\n3. Display Finished Tasks\n4. Quit")
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            add_task(todo_list)
        elif choice == '2':
            finish_task(todo_list, finished_tasks)
        elif choice == '3':
            display_finished_tasks(finished_tasks)
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
if __name__ == "__main__":
    main()
