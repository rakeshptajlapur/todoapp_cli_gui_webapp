import PySimpleGUI as rt

#creating the elements inside the gui interface
my_label = rt.Text("Enter the Todo item")
my_input_box = rt.InputText(tooltip="enter the item tex")
my_button = rt.Button("Add item")

#creating the gui interface
window = rt.Window("My first GUI App", layout=[[my_label], [my_input_box,my_button]])
window.read()
print("hello print")
print("hello print")
window.close()

