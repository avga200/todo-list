import functions
import PySimpleGUI as sg

label = sg.Text("Enter a to-do")
inputLabel = sg.InputText(tooltip="Enter a to-do", key="todo", do_not_clear=False)
add = sg.Button("ADD")
complete = sg.Button("COMPLETE")
edit = sg.Button("EDIT")
list_box = sg.Listbox(values=functions.get_todos(), key = 'todos', enable_events=True, size=[45,10])
exit = sg.Button('EXIT')
window = sg.Window("TO-DO List", layout=[[label, inputLabel],[add,complete,edit,exit],[list_box]], font=("Helvetica",13))

while True:
    event, value = window.read()
    print(event, value)
    match event:
        case 'ADD':
            if value['todo'].strip() == '':
                print("Enter a valid todo")
            else:
                functions.add(value['todo'])
                list_box.update(values= functions.get_todos())
        case 'COMPLETE':
            functions.complete(value['todos'])
            list_box.update(values=functions.get_todos())
        case 'EDIT':
            to_edit = value['todo']
            prev_val = value['todos']
            functions.edit(to_edit, prev_val[0])
            print(to_edit,prev_val)
            list_box.update(values=functions.get_todos())
        case 'EXIT':
            break
        case sg.WIN_CLOSED:
            break
window.close()