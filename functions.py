FILEPATH = 'todos.txt'


def get_todos(file_path=FILEPATH):
    """ Read a text file  and return  the list of  todo items """
    with open(file_path, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

#print(help(get_todos()))

# todos_arg string filepath list
def write_todos(todos_arg , filepath=FILEPATH ):
    #write the todo items list in the text file.
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)




if __name__ == '__main__':
    print(get_todos())