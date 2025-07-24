#TO DO LIST APPLICATION IN PYTHON USING LISTS, DICTIONATIES, FUNCTIONS AND CONDITIONAL STATEMENTS !

print()
print("--------------- Welecome to To-Do List App ---------------")
tasks = []
menu = ["Add Task", "View Tasks", "Mark task as completed", "Delete Task","Exit"]
for i,option in enumerate(menu):
    print(f'{i+1}. {option}')

def view_usr():
    if not tasks:
        print("No tasks Yet.")
    else:
        for i,task in enumerate(tasks):
            if task["done"]:
                status = "✅ Done"
            else:
                status = "❌ Not Done"
            print(f'{i+1}. {task["task"]} and status is {status}')
while True:
    usr_inp = input("Enter Your Option( 1-5 ): ")
    try:
        usr_inp =int(usr_inp)
        if usr_inp >= 1 and usr_inp <=5:
            if usr_inp == 1:
                print("You chose Add Task")
                name = input("Enter Name of the task: ")
                tasks.append({"task":name,"done": False})
                print(tasks)
            elif usr_inp == 2:
                print(" You chose View Tasks")
                print()
                print("----- Your Tasks -----")
                if not tasks:
                    print("No tasks yet. Add something!")
                else:
                    view_usr()  
            elif usr_inp == 3:
                print("You chose mark to done section")
                if not tasks:
                    print("No tasks to mark as completed!")
                else:
                    view_usr()
                    try:
                        task_index=int(input("Enter the number to Mark as Done: ")) -1
                        if task_index < 0 or task_index >=len(tasks):
                            print("Enter a number within range")
                        else:
                            tasks[task_index]["done"] =True
                            print(f"{tasks[task_index]["task"]} task is marked as done ✅.")
                            print()
                            view_usr()
                    except:
                        print("Invalid input. Please enter a number.")
            elif usr_inp == 4:
                print("Delete Task")
                print("You chose to delete tasks")
                if not tasks:
                    print("No tasks to delete!")
                else:
                    view_usr()
                    task_index=int(input("Enter the number to delete: ")) -1
                    if task_index < 0 or task_index >=len(tasks):
                        print("Enter a number within range")
                    else:
                        tasks.pop(task_index)
                        print(f"{tasks[task_index]["task"]} task is deleted successfully ✅.")
                        print()
                        view_usr()
            elif usr_inp == 5:
                print("Exit successfully!")
                break
        else:
            print("Enter a valid option")
    except:
        print("Don't Enter strings or Float!")




