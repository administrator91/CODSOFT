import datetime
print("\n\t------------------------------------------------------------------")
print("\n\t   Hey Buddy!! This is a T0-Do List Program made By Rajarshi.. ")
print("\t             With help of Python Programming Language..            \n")
print("\t------------------------------------------------------------------\n")

tasks = {}
#Task add here
def add_task():
    task_description = input("Enter task description: ")
    due_date_str = input("Enter due date (YYYY-MM-DD, optional): ")
    
    if due_date_str:
        due_date = datetime.datetime.strptime(due_date_str, "%Y-%m-%d").date()
    else:
        due_date = None
    
    task_id = len(tasks) + 1
    task = {
        'description': task_description,
        'due_date': due_date,
        'status': 'Incomplete'
    }
 #successfully add task.............
    tasks[task_id] = task
    print(f'Task {task_id} added successfully!\n')
#View here.....
def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        for task_id, task in tasks.items():
            print(f"{task_id}. {task['description']} - Due: {task['due_date']} - Status: {task['status']}")
    print()
#Task complete mark.....
def mark_completed():
    view_tasks()   #cause if there is no task nad which task you want to mark... so need view_task fun..
    task_id = int(input("\tEnter the task number to mark as completed: "))
    
    if task_id in tasks:
        tasks[task_id]['status'] = 'Completed'
        print(f'Task {task_id} marked as completed!\n')
    else:
        print("Invalid task number.\n")

#INTRF here.....
while True:
    print("\n\t____________To-Do List Application____________")
    print("\t               1. Add Task                    ")
    print("\t               2. View Tasks                  ")
    print("\t               3. Mark Task as Completed      ")
    print("\t               4. Exit                        ")
    #User Choose here...
    choice = input("\n   Enter your choice (1-4): ")
    
    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        mark_completed()
    elif choice == '4':
        print("Exiting the To-Do List Application...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 to 4....\n")
