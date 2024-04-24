def display_menu():
    print("Menu:")
    print("1. Add task")
    print("2. view tasks")
    print("3. Mark as done")
    print("4. Exit")

def add_task(tasks):
    task=input("Enter the task description: ")
    tasks.append(task)
    print("Sucessfully task added")

def view_tasks(tasks):
    print("\nTasks:")
    for i, task in enumerate(tasks,start=1):
        print(f"{i}.{task}")

def mark_task_done(tasks):
    if not tasks:
        print("no task to mark as done.")
        return

    view_tasks(tasks)
    index=int(input("enter task index to mark as done: "))-1

    if 0<= index< len(tasks):
        removed_task=tasks.pop(index)
        print(f"task '{removed_task} marked as done and removed")
    else:
        print("invalid task index: ")

def save_tasks(tasks):
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task+'\n')

def load_tasks():
    try:
        with open("tasks.txt","r") as f:
            return
        f.read().splitlines()
    except FileNotFoundError:
        return []

def main():
    tasks=load_tasks()

    while True:
        display_menu()

        choice=input("enter your choice: ") 

        if choice=='1':
            add_task(tasks)
        elif choice=='2':
            view_tasks(tasks) 
        elif choice=='3':
            mark_task_done(tasks)
        elif choice=='4':
            print("exiting")
            save_tasks(tasks)
            break
        else:
            print("invalid choice please select a valid option.")

if __name__=="__main__":
    main()

                                                 