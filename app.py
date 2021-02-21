from Tkinter import *
import ttk


# intiate tkinter
root = Tk()
root.title('Okumara/Hata model to predict the path loss')


def centerWindow(width, height=200):
    # get screen width and height
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screenHeight / 2) + (-100)
    y = (screenHeight / 2) - (height / 2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))


centerWindow(750, 600)

# custom style
style = ttk.Style()
style.configure('TEntry', foreground='green')

# all input fields variables
carrierFrequency = StringVar()
antennaheightT = StringVar()
antennaheightR = StringVar()


# Heading
ttk.Label(root,
          text='Enter the all specified values',
          font=('Helvetica', 20),
          foreground="blue").grid(column=1, row=5, padx=20, pady=20)

# carrier frequency
ttk.Label(root,
          anchor="e",
          justify=LEFT,
          text='value of carrier frequency(150-1500 in MHz)      :',
          font=('Times new Roman', 15),
          foreground="black").grid(column=1, row=6, padx=20, pady=10)

carrierFrequencyField = ttk.Entry(root,
                                  width=20,
                                  textvariable=carrierFrequency,
                                  justify=CENTER,
                                  font=('Times new Roman', 15, 'bold'))

carrierFrequencyField.focus_force()
carrierFrequencyField.grid(column=2, row=6)


# height of transmitter antenna
ttk.Label(root,
          text='height of transmitter antenna(30 - 300 in meter)  :',
          font=('Times new Roman', 15),
          foreground="black").grid(column=1, row=7, padx=20, pady=10)

antennaheightFieldT = ttk.Entry(root,
                                width=20,
                                textvariable=antennaheightT,
                                justify=CENTER,
                                font=('Times new Roman', 15, 'bold'))

antennaheightFieldT.focus_force()
antennaheightFieldT.grid(column=2, row=7)

# height of receiver antenna
ttk.Label(root,
          text='height of receiver antenna (1 - 10 in meter)          :',
          font=('Times new Roman', 15),
          foreground="black").grid(column=1, row=8, padx=20, pady=10)

antennaheightFieldR = ttk.Entry(root,
                                width=20,
                                textvariable=antennaheightR,
                                justify=CENTER,
                                font=('Times new Roman', 15, 'bold'))

antennaheightFieldR.focus_force()
antennaheightFieldR.grid(column=2, row=8)

#  '


# all input field to take the data from user
# ttk.Label(root, text='Select the type of city',
#           font=('Times new Roman', 15), foreground="blue").grid(column=3, row=5, padx=10, pady=25)
# options = ['Small/Medium', 'Large']


# def citySelected(event):
#     myLabel = Label(root, text=selectedCity.get())

# selectedCity = StringVar()
# selectedCity.set(options[0])

# cityTypeOptionsMenu = OptionMenu(
#     root, selectedCity, *options, command=citySelected)
# cityTypeOptionsMenu.grid(column=4, row=5)


root.mainloop()
