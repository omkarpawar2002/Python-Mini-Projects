# Build A To-do-List By Using List Data Structure


task_list = []

while True:
    choice = int(input("==== To-Do-List ===="\
                       "\n 1.ADD TASK "\
                       "\n 2.DELETE TASK "\
                       "\n 3.VIEW PARTICULAR TASK "\
                       "\n 4.VIEW ALL TASKS "\
                       "\n 5.TOTAL TASK "\
                       "\n 6.EXIT :- "))
    if(choice == 1):
        num = int(input("Enter how many task you want to add :- "))
        for i in range(num):
            task_dict = {}
            print("=========================")
            task_id = int(input("Enter task id : "))
            task_name = input("Enter Task Here :- ")
            task_status = False
            task_priority = input("Enter Task Priority i.e.,High or Low :- ")
            task_dict.update({"task_id":task_id,"task_name":task_name,"task_status":task_status,"task_priority":task_priority})
            task_list.append(task_dict)
    elif(choice == 2):
        if(task_list):
            check_id = int(input("Enter Id :- "))
            for tasks in task_list:
                if(check_id == tasks["task_id"]):
                    task_list.remove(tasks)
                    print("=========================")
                    print("Task Deleted Successfully!!")
                    print("=========================")
                    break
                else:
                    continue
            else:
                print("=========================")
                print("No Task Match!!")
                print("=========================")
        else:
            print("========================")
            print("No Task Available To Delete!!")    
            print("========================")
    elif(choice == 3):
        if(task_list):
            check_id = int(input("Enter Id :- "))
            for tasks in task_list:
                if(check_id == tasks["task_id"]):
                    print("=========================")
                    for key,value in tasks.items():
                        print(f"{key} = {value}")
                    print("=========================")
                    break
                else:
                    continue
            else:
                print("=========================")
                print("No Task Match!!")
                print("=========================")
        else:
            print("========================")
            print("No Task Available!!")    
            print("========================")
    elif(choice == 4):
        if(task_list):
            for tasks in task_list:
                print("========================")
                for key,value in tasks.items():
                    print(f"{key} = {value}")
        else:
            print("========================")
            print("No Task Available!!")    
            print("========================")
    elif(choice == 5):
        print("========================")
        print(f"Total tasks {len(task_list)}")
        print("========================")
    elif(choice == 6):
        print("========================")
        print("Thank You For Using To-Do-List Application")
        print("========================")
        break
    else:
        print("========================")
        print("Incorrect Choice!!!")
        print("========================")