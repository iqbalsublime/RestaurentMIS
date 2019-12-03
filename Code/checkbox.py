import tkinter
from tkinter import *

master = tkinter.Tk()
master.geometry("750x500")

listbox = Listbox(master)
listbox.place(x=3, y=0)

gui_state = {
    "one": {
        'button 1': BooleanVar(),
        'button 2': BooleanVar(),
        'button 3': BooleanVar(),
    },
    "two": {
        'button 1': BooleanVar(),
        'button 2': BooleanVar(),
        'button 3': BooleanVar(),
    },
    "three": {
        'button 1': BooleanVar(),
        'button 2': BooleanVar(),
        'button 3': BooleanVar(),
    },
    "four": {
        'button 1': BooleanVar(),
        'button 2': BooleanVar(),
        'button 3': BooleanVar(),
    },
}

for item in gui_state.keys():
    listbox.insert(END, item)


def bind_checkboxen(master, category):
    # render checkboxes for category. Mutate category when checkboxes are toggled.
    global checkboxes

    # delete old checkboxes
    for checkbox in checkboxes:
        checkbox.destroy()
    checkboxes = []

    x = 0

    # create new ones based on category fields
    for key in category.keys():
        checkbox = Checkbutton(master, text=key, variable=category[key])
        checkbox.place(x=300, y=0 + x)
        checkboxes.append(checkbox)
        x += 50


checkboxes = []


def onselect(evt):
    # Note here that Tkinter passes an event object to onselect()
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    print('You selected item %d: "%s"' % (index, value))
    bind_checkboxen(master, gui_state[value])


listbox.bind('<<ListboxSelect>>', onselect)

mainloop()