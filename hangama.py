from Tkinter import *

window = Tk()

name_array = [('a1', 'a2', 'a3'), ('b1', 'b2', 'b3'),
              ('c1', 'c2', 'c3'), ('d1', 'd2', 'd3')]
position_track = IntVar()

first_name = StringVar()
last_name = StringVar()
email = StringVar()


def return_value(pos):
    first_name.set(name_array[pos][0])
    last_name.set(name_array[pos][1])
    email.set(name_array[pos][2])


def update_value(pos):
    name_array[pos] = (first_name.get(), last_name.get(), email.get())


def first_value():
    global position_track
    return_value(0)
    position_track.set(0)


def last_value():
    global position_track
    return_value(-1)
    position_track.set(-1)


def next_value():
    global position_track
    if position_track.get() == len(name_array):
        position_track.set(1)
    temp = position_track.get()
    return_value(temp + 1)
    position_track.set(temp + 1)


def prev_value():
    global position_track
    if position_track.get() == -1:
        position_track.set(len(name_array) - 1)
    temp = position_track.get()
    return_value(temp - 1)
    position_track.set(temp - 1)


label_first_name = Label(window, text='First Name:', justify='right', padx=5)
entry_first_name = Entry(window, textvariable=first_name)
label_last_name = Label(window, text='Last Name:', justify='right', padx=5)
entry_last_name = Entry(window, textvariable=last_name)
label_email = Label(window, text='Email Address:', justify='right', padx=5)
entry_email = Entry(window, textvariable=email)


button_first = Button(window, text='First', command=first_value)
button_last = Button(window, text='Last', command=last_value)
button_prev = Button(window, text='Prev', command=prev_value)
button_next = Button(window, text='Next', command=next_value)
button_quit = Button(window, text='Quit')
button_quit.configure(command=window.destroy)

labels = [label_first_name, label_last_name, label_email]
entries = [entry_first_name, entry_last_name, entry_email]
buttons = [button_first, button_last, button_prev,
           button_next, button_last, button_quit]


for i in range(3):
    labels[i].grid(row=i, column=0, sticky='W')
    entries[i].grid(row=i, column=1, columnspan=6)

for j in range(6):
    buttons[j].grid(row=3, column=j, sticky='E')

window.mainloop()
