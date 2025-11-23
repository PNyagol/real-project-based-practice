task_list = []

def add_item():
    enter_task = input("Enter Task: ")
    task_list.append(enter_task)

def remove_item():
    view_tasks()
    try:
        task_num = int(input("Enter number of task you want to REMOVE: "))
        if 1 <= task_num <= len(task_list):
            removed_task = task_list.pop(task_num - 1)
            print(f"Removed task: '{removed_task}'")
        else:
            print("Oops! Invalid Task number")
    
    except ValueError:
        print("Please enter a valid number")

def view_tasks():
    if not task_list:
        print("Your to-do list is empty...")
    else:
        print("\nYour To-Do List: ")
        for index, task in enumerate(task_list, start=1):
            print(f'{index} | {task}')
        print()

while True:
    print("Menu")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_item()
        elif choice == 2:
            remove_item()
        elif choice == 3:
            view_tasks()
        elif choice == 4:
            break
        else:
            print("Oops! Invalid Choice. Try Again")
    except ValueError:
        print("Please enter a valid number")