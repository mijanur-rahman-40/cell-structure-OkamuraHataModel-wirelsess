from Tkinter import *
import ttk
from src.HataModel import OkamuraHataModel

# import sys
# from os import path
# sys.path.append('../src')
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
selectedCityValue = IntVar(value=1)
selectedAreaValue = IntVar(value=1)


headingfontTypeAndSize = ('Helvetica', 20)
# labels
labelsfontTypeAndSize = ('Times new Roman', 14)

# text filed
textFiledFont = ('Times new Roman', 15, 'bold')

# Heading
labelHeading = Label(root,
                     text='Enter the all specified values',
                     font=headingfontTypeAndSize,
                     foreground="blue")

# carrier frequency
labelCarrierFrequency = Label(root,
                              text='Value of carrier frequency(150-1500 in MHz)        :',
                              font=labelsfontTypeAndSize,
                              foreground="black")

carrierFrequencyField = ttk.Entry(root,
                                  width=16,
                                  textvariable=carrierFrequency,
                                  justify=CENTER,
                                  font=textFiledFont)

carrierFrequencyField.focus_force()

# height of transmitter antenna
labelantennaheightT = Label(root,
                            text='Height of transmitter antenna(30 - 300 in meter)    :',
                            font=labelsfontTypeAndSize,
                            foreground="black")

antennaheightFieldT = ttk.Entry(root,
                                width=16,
                                textvariable=antennaheightT,
                                justify=CENTER,
                                font=textFiledFont)

antennaheightFieldT.focus_force()

# height of receiver antenna
labelAntennaheightR = Label(root,
                            text='Height of receiver antenna (1 - 10 in meter)           :',
                            font=labelsfontTypeAndSize,
                            foreground="black")

antennaheightFieldR = ttk.Entry(root,
                                width=16,
                                textvariable=antennaheightR,
                                justify=CENTER,
                                font=textFiledFont)

antennaheightFieldR.focus_force()

# Propagation distance
labelPropagationDistance = Label(root,
                                 text='Propagation distance between antennas (1 - 20 in km) :',
                                 font=labelsfontTypeAndSize,
                                 foreground="black")

propagationDistanceField = ttk.Entry(root,
                                     width=16,
                                     textvariable=propagationDistance,
                                     justify=CENTER,
                                     font=textFiledFont)

propagationDistanceField.focus_force()


# Option menu of type of city
labelCityType = Label(root,
                      text='Select the type of city',
                      font=labelsfontTypeAndSize,
                      foreground="black")

cityOptions = ['Small/Medium', 'Large']


def citySelected(event):
    selectedCityValue.set(1 if selectedCity.get() == 'Small/Medium' else 2)


selectedCity.set(cityOptions[0])
cityTypeOptionsMenu = OptionMenu(
    root,
    selectedCity,
    *cityOptions,
    command=citySelected)

cityTypeOptionsMenu.config(width=15)


# Option menu of type of area
labelAreaType = Label(root,
                      text='Select the type of area',
                      font=labelsfontTypeAndSize,
                      foreground="black")

areaOptions = ['Urban/Suburban', 'Open area']


def areaSelected(event):
    selectedAreaValue.set(1 if selectedArea.get() == 'Urban/Suburban' else 2)


selectedArea.set(areaOptions[0])

areaTypeOptionsMenu = OptionMenu(
    root,
    selectedArea,
    *areaOptions,
    command=areaSelected)

areaTypeOptionsMenu.config(width=15)


def getPathLoss():
    okamura_hata_model = OkamuraHataModel(
        carrierierFrequency=int(carrierFrequency.get()),
        heightTransmitter=int(antennaheightT.get()),
        heightReceiver=int(antennaheightR.get()),
        linkDistance=int(propagationDistance.get()),
        city=selectedCityValue.get(),
        area=selectedAreaValue.get()
    )

    ttk.Label(root,
              text="Path loss (in dB):" +
              str(okamura_hata_model.pathLoss) + 'dB',
              font=textFiledFont,
              foreground="black").grid(column=1, row=12, padx=20, pady=20)


myButton = Button(root, text='Get Path Loss',
                  command=getPathLoss, fg='white', bg='blue', font=labelsfontTypeAndSize)

labels = [labelHeading, labelCarrierFrequency, labelantennaheightT,
          labelAntennaheightR, labelPropagationDistance, labelCityType, labelAreaType, myButton]

fields = [carrierFrequencyField, antennaheightFieldT,
          antennaheightFieldR, propagationDistanceField, cityTypeOptionsMenu, areaTypeOptionsMenu]

for i in range(8):
    labels[i].grid(row=i, column=1, sticky='W', padx=20, pady=10)

for i in range(6):
    fields[i].grid(row=i + 1, column=2)

root.mainloop()
