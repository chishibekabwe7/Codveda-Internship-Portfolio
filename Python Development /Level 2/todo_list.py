# To-Do List Application
# Codveda Internship - Level 2
# Author: Chishibe Kabwe

import json
import os
from datetime import datetime

DATA_FILE = "tasks.json"


def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if not content:
                return []
            return json.loads(content)
    except (json.JSONDecodeError, IOError):
        print("Warning: Task file is corrupted or unreadable. Starting fresh.")
        return []


def save_tasks(tasks):
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(tasks, f, indent=2)
    except IOError as e:
        print(f"Error saving tasks: {e}")


def get_next_id(tasks):
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1


def add_task(tasks):
    description = input("Enter task description: ").strip()

    if not description:
        print("Task description cannot be empty.\n")
        return

    task = {
        "id": get_next_id(tasks),
        "description": description,
        "completed": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added with ID {task['id']}.\n")


def view_tasks(tasks):
    if not tasks:
        print("No tasks found.\n")
        return

    print("\n" + "-" * 50)
    print(f"{'ID':<5}{'Status':<12}{'Description':<25}{'Created'}")
    print("-" * 50)

    for task in tasks:
        status = "Done" if task["completed"] else "Pending"
        print(f"{task['id']:<5}{status:<12}{task['description']:<25}{task['created_at']}")

    print("-" * 50 + "\n")


def find_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None


def get_task_id_input(prompt):
    raw = input(prompt).strip()
    try:
        return int(raw)
    except ValueError:
        print("Invalid ID. Please enter a number.\n")
        return None


def mark_task_done(tasks):
    if not tasks:
        print("No tasks available.\n")
        return

    view_tasks(tasks)
    task_id = get_task_id_input("Enter the ID of the task to mark as done: ")

    if task_id is None:
        return

    task = find_task(tasks, task_id)

    if task is None:
        print(f"No task found with ID {task_id}.\n")
        return

    if task["completed"]:
        print(f"Task {task_id} is already marked as done.\n")
        return

    task["completed"] = True
    save_tasks(tasks)
    print(f"Task {task_id} marked as done.\n")


def delete_task(tasks):
    if not tasks:
        print("No tasks available.\n")
        return

    view_tasks(tasks)
    task_id = get_task_id_input("Enter the ID of the task to delete: ")

    if task_id is None:
        return

    task = find_task(tasks, task_id)

    if task is None:
        print(f"No task found with ID {task_id}.\n")
        return

    tasks.remove(task)
    save_tasks(tasks)
    print(f"Task {task_id} deleted.\n")


def display_menu():
    print("=" * 50)
    print("                 TO-DO LIST")
    print("=" * 50)
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Exit")
    print("-" * 50)


def main():
    tasks = load_tasks()

    while True:
        display_menu()
        choice = input("Select an option (1-5): ").strip()
        print()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Invalid option. Please choose between 1 and 5.\n")


if __name__ == "__main__":
    main()