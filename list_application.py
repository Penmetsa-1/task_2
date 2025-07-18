# todo.py
# Author: Sandeep (Intern @ BrokiesHub - pyInt Program)
# Description: Console-based To-Do List Application with persistent storage.

# File used for storing tasks persistently
FILENAME = "tasks.txt"


# ------------------------ Utility Functions ------------------------

def load_tasks():
    """
    Load tasks from the file into a list.
    Returns a list of task strings.
    """
    try:
        with open(FILENAME, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        # If file doesn't exist, return an empty list
        return []


def save_tasks(tasks):
    """
    Save all tasks from the list to the file.
    Overwrites the existing content in the file.
    """
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")


# ------------------------ Task Operations ------------------------

def view_tasks(tasks):
    """
    Display all tasks with their status.
    """
    if not tasks:
        print("📭 Your to-do list is empty.")
    else:
        print("\n📝 Your To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")


def add_task(tasks):
    """
    Prompt user to add a task and append it to the list.
    """
    task = input("Enter the task to add: ").strip()
    tasks.append(f"[ ] {task}")
    print(f"✅ '{task}' has been added.")


def remove_task(tasks):
    """
    Prompt user to remove a task by its number.
    """
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to remove: "))
        removed = tasks.pop(task_num - 1)
        print(f" ' '{removed}' has been removed.")
    except (ValueError, IndexError):
        print("⚠️ Invalid task number. Please try again.")


def mark_completed(tasks):
    """
    Mark a selected task as completed (checkbox style).
    """
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to mark as completed: "))
        task = tasks[task_num - 1]
        if "[x]" in task:
            print("ℹ️ Task is already marked as completed.")
        else:
            tasks[task_num - 1] = task.replace("[ ]", "[x]", 1)
            print("✅ Task marked as completed.")
    except (ValueError, IndexError):
        print("⚠️ Invalid task number.")


def search_tasks(tasks):
    """
    Search for tasks containing a specific keyword.
    """
    keyword = input("Enter keyword to search: ").lower()
    found = [task for task in tasks if keyword in task.lower()]
    if found:
        print("\n🔍 Search Results:")
        for task in found:
            print(task)
    else:
        print("❌ No matching tasks found.")


def clear_tasks(tasks):
    """
    Clear all tasks from the list after user confirmation.
    """
    confirm = input("Are you sure you want to delete all tasks? (yes/no): ")
    if confirm.lower() == "yes":
        tasks.clear()
        print("🧹 All tasks have been cleared.")
    else:
        print(" Operation cancelled.")


# ------------------------ Main Program Loop ------------------------

def main():
    """
    Main menu loop to handle user interaction and actions.
    """
    tasks = load_tasks()
    while True:
        print("\n To-Do List Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Mark Task as Completed")
        print("5. Search Tasks")
        print("6. Clear All Tasks")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            mark_completed(tasks)
        elif choice == '5':
            search_tasks(tasks)
        elif choice == '6':
            clear_tasks(tasks)
        elif choice == '7':
            save_tasks(tasks)
            print("💾 Tasks saved. Goodbye! 👋")
            break
        else:
            print("⚠️ Invalid choice. Please enter a number between 1 and 7.")


# ------------------------ Program Entry Point ------------------------

if __name__ == "__main__":
    main()
