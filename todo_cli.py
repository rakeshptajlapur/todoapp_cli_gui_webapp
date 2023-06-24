
my_todo_list = []
while True:
    user_promt = input("add,show,edit,complete,exit : ")
    if user_promt == "add":
            my_todo_item = input("enter the todo item : ")
            my_todo_list.append(my_todo_item)
            print(my_todo_item + " item added to the list")
    elif user_promt == "show":
            for x,i in enumerate(my_todo_list):
                print(str(x) + "-" + i)
    elif user_promt == "edit":
            for x,i in enumerate(my_todo_list):
                print(str(x) + "-" + i)
            edit_index = int(input("enter the index of todo item to edit :"))
            edit_item = str(input("enter the new todo item to replace the old :"))
            my_todo_list[edit_index] = edit_item
            print(edit_item + " has been added/edited to the todo list" )
    elif user_promt == "complete":
            for x, i in enumerate(my_todo_list):
                print(str(x) + "-" + i)
            complete_index = int(input("enter the index of item you want to mark completed :"))
            del my_todo_list[complete_index]
            print("Have marked it as complete !")
    elif user_promt == "exit":
            print("thankyou, bye!")
            exit()
    else:
        print("Invalid command")

