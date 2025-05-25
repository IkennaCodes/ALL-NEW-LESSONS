print("--- To-Do List Menu ---")

tasks = []
while True:

    print ("1. View Tasks")
    print ("2. Add A Task")
    print ("3. Remove A Task")
    print ("4. Exit")
    user_choice = int(input("Choose an option (1-4): "))



    if user_choice == 1:
        if not tasks:
            print("You have no tasks.")
        else:
            print("Here are your tasks:")
            print(tasks)

    elif user_choice == 2:
        new_task = input("What task do you want to add? ")
        tasks.append(new_task)
        print("Added:", new_task)


    
    elif user_choice == 3:
        if not tasks:
            print("No tasks to delete!")
        index_delete = int(input("Enter the task's index you want deleted"))
        deleted = tasks.pop(index_delete)
        print("Deleted:", deleted)

    elif user_choice == 4: 
        print("Goodbye!")
        break

    else:
        print("Invalid Option")
