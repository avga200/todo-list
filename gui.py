import functions
import PySimpleGUI as sg

label = sg.Text("Enter a to-do")
inputLabel = sg.InputText(tooltip="Enter a to-do")
add = sg.Button("ADD")
complete = sg.Button("COMPLETE")
edit = sg.Button("EDIT")
window = sg.Window("TO-DO List", layout=[[label, inputLabel],[add,complete,edit]])

window.read()

window.close()