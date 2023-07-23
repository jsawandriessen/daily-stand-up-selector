import functions
import PySimpleGUI as sg
import random

# start with the whole group in random order
initial_members = functions.get_all_members()
random.shuffle(initial_members)

label = sg.Text("Who will be next?")
input_box = sg.InputText("Who will go first?", key="next_person")
next_button = sg.Button("Next")
list_box = sg.Listbox(values=initial_members, key="members",
                      enable_events=True, size=[65, 15])
edit_button = sg.Button("Edit")

window = sg.Window('My random people selector App',
                   layout=[[label],
                           [input_box, next_button],
                           [list_box]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)

    match event:

        case "Next":
            people_list = initial_members

            if len(people_list) > 0:
                next_person = functions.select_next_person(people_list)
                window["next_person"].update(value=next_person)
                people_list.remove(next_person)
                window["members"].update(values=people_list)
            else:
                break

        case sg.WINDOW_CLOSED:  # Breaks while loop when quit icon is being pressed
            break


window.close()
