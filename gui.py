import functions
import PySimpleGUI as SimpleGUI
import time


def window_elements():
    label_time = SimpleGUI.Text(time.strftime('%d %B %Y'))
    label = SimpleGUI.Text("Enter a to-do")
    input_label = SimpleGUI.InputText(tooltip="Enter a to-do", key="todo", do_not_clear=False)
    add = SimpleGUI.Button("ADD")
    complete = SimpleGUI.Button("COMPLETE")
    edit = SimpleGUI.Button("EDIT")
    list_box = SimpleGUI.Listbox(values=functions.get_todos(), key='todos', enable_events=True, size=(40, 5))
    cross = SimpleGUI.Button('EXIT')
    create_window = SimpleGUI.Window("TO-DO List",
                                     layout=[[label_time], [label, input_label], [add, complete, edit, cross],
                                             [list_box]],
                                     font=("Helvetica", 13))
    return create_window


window = window_elements()
while True:
    event, value = window.read()
    print(event, value)
    match event:
        case 'ADD':
            if value['todo'].strip() == '':
                print("Enter a valid todo")
            else:
                functions.add_todo(value['todo'])
                window['todos'].update(values=functions.get_todos())
        case 'COMPLETE':
            functions.complete(value['todos'])
            window['todos'].update(values=functions.get_todos())
        case 'EDIT':
            to_edit = value['todo']
            try:
                prev_val = value['todos'][0]
            except IndexError:
                print('choose a to-do')
            functions.edit_todo(to_edit, prev_val)
            window['todos'].update(values=functions.get_todos())
        case 'EXIT' | SimpleGUI.WIN_CLOSED:
            break
window.close()
