todo_list = []

def show_todo_list():
    for x, y in enumerate(todo_list):
        print(str(x + 1) + "-" + y)
def add_todo_list(add_item):
    todo_list.append(add_item)
    print(add_item + " has been added to todo list successfully!")

def edit_todo_list(index_number_to_edit, to_be_edited_value):
    actual_index = int(index_number_to_edit) - 1
    todo_list[actual_index] = to_be_edited_value
    print(to_be_edited_value + "has been added in the index " + index_number_to_edit + " successfully!")

def delete_todo_list(index_number_to_remove):
            actual_index_to_remove = index_number_to_remove - 1
            print(todo_list[actual_index_to_remove] + " has been marked completed and removed! ")
            del todo_list[actual_index_to_remove]




while True:
    user_action = input("Actions - add, show, edit, complete, exit : ")
    match user_action:
        case "add":
            add_item = str(input("enter the todo item you want to add :"))
            add_todo_list(add_item)

        case "show":
            show_todo_list()

        case "edit":
            show_todo_list()
            index_number_to_edit = input("enter the index which you want to edit :")
            to_be_edited_value = str(input("enter the new value for editing :"))
            edit_todo_list(index_number_to_edit, to_be_edited_value)

        case "complete":
            show_todo_list()
            index_number_to_remove = int(input("enter index of completed item : "))
            delete_todo_list(index_number_to_remove)


        case "exit":
            break



