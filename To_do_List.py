tasks = []

def add_task():
    tsk = input("Enter the Task : ")
    tasks.append({"task":tsk,"completed":False})
    print("Your Task Added Successfully")

def delete_task():
    print()
    View_task()
    print()
    task_no = int(input("Enter the number which task you want to Delete : "))
    if 1 <= task_no <= len(tasks): 
       tasks.pop(task_no-1)
       print("Your Task is  Deleted Successfully")
    else:
        print("Invalid Task Number")   

def Update_task():
    print()
    View_task()
    print()
    task_no = int(input("Enter the number which task you want to Update : "))
    if 1 <= task_no <= len(tasks): 
       new_task = input("Enter the New Task : ")
       tasks[task_no-1]["task"] = new_task
       print("Your Task is  Updated Successfully")
    else:
        print("Invalid Task Number") 

def View_task():
    if not tasks:
        print("Your To-Do List is Empty")
    else:
        print("YOUR TO-DO LIST")
        print()
        for index,task in enumerate(tasks,start=1):
             status = "completed" if task["completed"] else "Pending"
             print(f"{index}. {task['task']} - {status}")   
        print()     

def Mark_Completed():
    print()
    View_task()
    print()
    task_no = int(input("Enter the number which task you want to Mark Completed : "))
    if 1 <= task_no <= len(tasks): 
       tasks[task_no-1]["completed"] = True
       print("Your Task is Successfully Marked Completed")
    else:
        print("Invalid Task Number") 

def main():
    while True:
        print("1.Adding the Task\n2.Updating the Task\n3.Deleting the Task\n4.Viewing the Task\n5.Marked Completed\n6.Exit")
        choice = int(input("Enter the Choice : "))

        if choice == 1:
            add_task()
        elif choice == 2:
            Update_task()
        elif choice == 3:
            delete_task()
        elif choice == 4:
            View_task()
        elif choice == 5:
            Mark_Completed()
        elif choice == 6:
            print("GoodBye have a Nice Day, Thank you") 
            break
        else:
            print("Invalid Number, Please! Enter the Valid Number")                      

if __name__ == '__main__':
    main()