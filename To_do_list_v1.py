tasks = []

def menu():
    print("="*22)
    print(" "*4,"To do List"," "*4)
    print("="*22)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    return choice

def Add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added successfully")
    confirmation = input("Do you want to add another task: y/n: ").lower()
    if confirmation == 'y':
        anot = input("Enter task: ")
        tasks.append(anot)
        print("Task added successfully")
        return

    return

def delete_task():
    if not tasks:
        print("No tasks available.")
        return
    for number, task in enumerate(tasks, start= 1):
        print(number,task)

    try:

        task = int(input("Enter task number to Delete task: "))
        if task < 1 or task > len(tasks):
            print("Invalid task number.")
            return
    
        tasks.pop(task-1)
        print("Task deleted successfully.")

    except ValueError:
        print("Please enter a number.")


def view_task():
    if not tasks:
        print("No tasks available.")
        return
    for number, task in enumerate(tasks, start= 1):
        print(number,task)


while True:
    choice = menu()

    if choice == 1:
        Add_task()

    elif choice == 2:
        view_task()

    elif choice == 3:
        delete_task()

    elif choice == 4:
        print("Exiting the program...\nthankyou.....")
        break

    else:
        print("Invalid choice")