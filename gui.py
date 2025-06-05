import os.path

import functions

import FreeSimpleGUI as sg
import time


if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass
sg.theme("DarkGrey13")


clock = sg.Text("",key='clock')
label = sg.Text("Type in a to-do")
input_box =sg.InputText(tooltip="enter todo", key= "todo")
add_button = sg.Button("Add")#image_soure = "add.png" size=2, mouseover_colors="DarkPurple" tooltip="Add todo"
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])

edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

# the reason for the [label] and [input_box] is to like distinguish them in sepearate lines
window = sg.Window(title='My to-do app',
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box,edit_button,complete_button],
                           [exit_button]],
                   font=("Helvetica", 10))
while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime('ime%b %d, %Y %H:%M:%S'))
    print(1, event)
    print(2, values)
    print(3, values['todos'])
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item",font=("Helvetica",15))


        case 'todos':
            window['todo'].update(value=values['todos'])
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]# apparently the [0] extracts string from the list
                todos = functions.get_todos()# gives us all the todos in the todos.txt file
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)# put the updated list
                window['todo'].update(value="")
            except IndexError:
                sg.popup("Please select an item",font=("Helvetica",15))

        case "Exit":
            break


        case sg.WIN_CLOSED:
            break


window.close()
