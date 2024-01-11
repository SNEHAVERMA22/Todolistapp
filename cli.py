# from functions import get_todos,write_todos
import functions
import time

now = time.strftime("%b %d,%Y %H: %M :%S")
print("It is",now)

while True:

    user_action = input("Type add,show,edit,complete and exit:")
    user_action = user_action.strip()

# user_action.startswith("add"):
    if user_action[0:3] == 'add':
        todo = user_action[4:]
        todo = todo + ("\n")

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos)


    elif user_action[0:4] == 'show':
        todos = functions.get_todos()
        # new_todo=[item.strip('\n') for item todos]

        for index, item in enumerate(todos):
            item=item.strip("\n")
            row=f"{index+1}-{item}"
            print(row)

    elif user_action[0:4]=='edit':
        try:
            number = int(user_action[5:])
            print(number)
            new_todo = input("enter new todo:")

            todos = functions.get_todos()

            todos[number - 1] = new_todo
            functions.write_todos(todos)


        except ValueError:
            print("Your command is invalid.")
            continue
    elif user_action[0:8] == 'complete':
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()
            todo_to_removed = todos[number - 1].strip('\n')
            todos.pop(number - 1)
            functions.write_todos(todos)
            message = f"todo{todo_to_removed} was removed from the list"
        except IndexError:
            print("The item is out of list.")
            continue


    elif user_action[0:4] == 'exit':
        break
    else:
        print("Command is invalid")

print("bye!!")








