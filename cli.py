password = input("Enter a password\n")

while password != 'pass123':
    password = input("Enter password")


from functions import get_todos, write_todos

import time

now = time.strft('ime%b %d, %Y %H:%M:%S')

print('it is',now,)

# of do import functions then functions.get_todos() something like that



while True:
    user_action = input('Type add,show, edit or exit\n')
    user_action = user_action.strip()


    if user_action.startswith('add'):

        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + '\n')

        write_todos(todos_arg=todos, filepath='todos.txt')

    elif user_action.startswith('show'):
        try:
            todos = get_todos(file_path='todos.txt')

            # makes a new todo list and strips the \n the loop provides
            # new_todo = []
            # for item in todos:
            #     new_item = item.strip('\n')
            #     new_todo.append(new_item)

            # Alternative(shorter code) LIST COMPREHENSION
            # new_todos = [item.strip('\n') for item in todos]

            for index, item in enumerate(todos):
                item = item.strip('\n')
                index = index + 1
                print(f"{index}.{item}")

        except ValueError:
            print("your command is not valid")
            continue





    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)


            number = number - 1



            todos = get_todos(file_path='todos.txt')

            new_todo = input("Enter new todo:")
            todos[number] = new_todo + '\n'

            write_todos(todos_arg=todos, filepath='todos.txt')

            print('here is how it will be',todos)
        except ValueError:
            print('Your command is not valid')
            continue


    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:].strip())

            todos = get_todos(file_path='todos.txt')

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            todos.pop(number - 1)

            write_todos(todos_arg=todos, filepath='todos.txt')
            message = f"todo {todo_to_remove} was removed"
            print(message)
        except IndexError:
            print(f"there is no item with that number ")
            continue

    elif user_action.startswith('exit'):
        break



    else:
        print('Try agaiin')