task_list = []

def add_item():
    enter_task = input("Enter Task: ")
    task_list.append({"task": enter_task, "done": False})

def remove_item():
    view_tasks()
    try:
        task_num = int(input("Enter number of task you want to REMOVE: "))
        if 1 <= task_num <= len(task_list):
            removed_task = task_list.pop(task_num - 1)
            print(f"Removed task: '{removed_task['task']}'")
        else:
            print("Oops! Invalid Task number")
    
    except ValueError:
        print("Please enter a valid number")

def view_tasks():
    if not task_list:
        print("Your to-do list is empty...")
    else:
        print("\nYour To-Do List: ")
        for index, task_item in enumerate(task_list, start=1):
            status = "✓" if task_item["done"] else "□"
            print(f'{index} | {status} {task_item["task"]}')
        print()


def mark_complete():
    view_tasks()
    try:
        task_num = int((input("Enter number of task you want to mark as complete: ")))
        if 1 <= task_num <= len(task_list):
            task_list[task_num - 1]["done"] = True
            print(f"✓ Marked as complete: '{task_list[task_num - 1]['task']}'")
        
        else:
            print("Ooops! Invalid Task number")


    except ValueError:
        print("Please enter a valid number")



while True:
    print("Menu")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Mark Task as Complete")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_item()
        elif choice == 2:
            remove_item()
        elif choice == 3:
            view_tasks()
        elif choice == 4:
            mark_complete()
        elif choice == 5:
            break
        else:
            print("Oops! Invalid Choice. Try Again")
    except ValueError:
        print("Please enter a valid number")