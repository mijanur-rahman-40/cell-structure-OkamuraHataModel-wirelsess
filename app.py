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


centerWindow(700, 600)

# custom style
style = ttk.Style()
style.configure('TEntry', foreground='green')

# all input fields variables
carrierFrequency = StringVar()
antennaheightT = StringVar()
antennaheightR = StringVar()
propagationDistance = StringVar()
selectedCity = StringVar()
selectedArea = StringVar()

# Heading
ttk.Label(root,
          text='Enter the all specified values',
          font=('Helvetica', 20),
          foreground="blue").grid(column=1, row=5, padx=20, pady=20)

# carrier frequency
ttk.Label(root,
          anchor="e",
          justify=LEFT,
          text='Value of carrier frequency(150-1500 in MHz)        :',
          font=('Times new Roman', 14),
          foreground="black").grid(column=1, row=6, padx=20, pady=10)

carrierFrequencyField = ttk.Entry(root,
                                  width=16,
                                  textvariable=carrierFrequency,
                                  justify=CENTER,
                                  font=('Times new Roman', 15, 'bold'))

carrierFrequencyField.focus_force()
carrierFrequencyField.grid(column=2, row=6)


# height of transmitter antenna
ttk.Label(root,
          text='Height of transmitter antenna(30 - 300 in meter)    :',
          font=('Times new Roman', 14),
          foreground="black").grid(column=1, row=7, padx=20, pady=10)

antennaheightFieldT = ttk.Entry(root,
                                width=16,
                                textvariable=antennaheightT,
                                justify=CENTER,
                                font=('Times new Roman', 15, 'bold'))

antennaheightFieldT.focus_force()
antennaheightFieldT.grid(column=2, row=7)

# height of receiver antenna
ttk.Label(root,
          text='Height of receiver antenna (1 - 10 in meter)           :',
          font=('Times new Roman', 14),
          foreground="black").grid(column=1, row=8, padx=20, pady=10)

antennaheightFieldR = ttk.Entry(root,
                                width=16,
                                textvariable=antennaheightR,
                                justify=CENTER,
                                font=('Times new Roman', 15, 'bold'))

antennaheightFieldR.focus_force()
antennaheightFieldR.grid(column=2, row=8)

# Propagation distance
ttk.Label(root,
          text='Propagation distance between antennas (1 - 20 in km) :',
          font=('Times new Roman', 14),
          foreground="black").grid(column=1, row=9, padx=20, pady=10)

propagationDistanceField = ttk.Entry(root,
                                     width=16,
                                     textvariable=propagationDistance,
                                     justify=CENTER,
                                     font=('Times new Roman', 15, 'bold'))

propagationDistanceField.focus_force()
propagationDistanceField.grid(column=2, row=9)


# Option menu of type of city
ttk.Label(root,
          text='Select the type of city',
          font=('Times new Roman', 15),
          foreground="black").grid(column=1, row=10, padx=20, pady=20)

cityOptions = ['Small/Medium', 'Large']

selectedCityValue = ''


def citySelected(event):
    selectedCityValue = selectedCity.get()


selectedCity.set(cityOptions[0])

cityTypeOptionsMenu = OptionMenu(
    root,
    selectedCity,
    *cityOptions,
    command=citySelected)

cityTypeOptionsMenu.config(width=15)
cityTypeOptionsMenu.grid(column=2, row=10)


# Option menu of type of area
ttk.Label(root,
          text='Select the type of area',
          font=('Times new Roman', 15),
          foreground="black").grid(column=1, row=11, padx=20, pady=20)

areaOptions = ['Urban/Suburban', 'Open area']

selectedAreaValue = ''


def areaSelected(event):
    selectedAreaValue = selectedArea.get()


selectedArea.set(areaOptions[0])

areaTypeOptionsMenu = OptionMenu(
    root,
    selectedArea,
    *areaOptions,
    command=areaSelected)

areaTypeOptionsMenu.config(width=15)
areaTypeOptionsMenu.grid(column=2, row=11)

# carrierFrequency = StringVar()
# antennaheightT = StringVar()
# antennaheightR = StringVar()
# propagationDistance = StringVar()
# selectedCity = StringVar()
# selectedArea = StringVar()


def getPathLoss():
    ttk.Label(root, text=int(carrierFrequency.get())).grid(
        column=1, row=12, padx=0, pady=10)


myButton = Button(root, text='Click me',
                  command=getPathLoss, padx=10, fg='white', bg='blue')
myButton.grid(column=1, row=15)


root.mainloop()
