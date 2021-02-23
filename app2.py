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

# label texts
allLabel = [
    'Enter the all specified values',
    'Value of carrier frequency(150-1500 in MHz)        :',
    'Height of transmitter antenna(30 - 300 in meter)    :',
    'Height of receiver antenna (1 - 10 in meter)           :',
    'Propagation distance between antennas (1 - 20 in km) :',
    'Select the type of city',
    'Select the type of area'
]

# font size and style
headingfontTypeAndSize = ('Helvetica', 20)
labelsfontTypeAndSize = ('Times new Roman', 14)
textFiledFont = ('Times new Roman', 15, 'bold')

# create  label
def createLabel(text, font, foregroundColor):
  return Label(root, text=text, font=font, foreground=foregroundColor)

# create input field
def createEntry(textvariable):
   return ttk.Entry(root, width=16, textvariable=textvariable, justify=CENTER, font=textFiledFont)

# all labels
for i in range(len(allLabel)):
    if i == 0:
        createLabel(allLabel[i], headingfontTypeAndSize, 'blue').grid(row=i, column=1, sticky='W', padx=20, pady=10)
    else:
        createLabel(allLabel[i], labelsfontTypeAndSize, 'black').grid(row=i, column=1, sticky='W', padx=20, pady=5)   
   

# all input fields
carrierFrequencyField = createEntry(carrierFrequency)
carrierFrequencyField.focus_force()
antennaheightFieldT = createEntry(antennaheightT)
antennaheightFieldT.focus_force()
antennaheightFieldR = createEntry(antennaheightR)
antennaheightFieldR.focus_force()
propagationDistanceField = createEntry(propagationDistance)
propagationDistanceField.focus_force()

# Option menu of type of city
cityOptions = ['Small/Medium', 'Large']

def citySelected(event):
    selectedCityValue.set(1 if selectedCity.get() == 'Small/Medium' else 2)

selectedCity.set(cityOptions[0])
cityTypeOptionsMenu = OptionMenu(root, selectedCity, *cityOptions, command=citySelected)
cityTypeOptionsMenu.config(width=15)

# Option menu of type of area
areaOptions = ['Urban/Suburban', 'Open area']

def areaSelected(event):
    selectedAreaValue.set(1 if selectedArea.get() == 'Urban/Suburban' else 2)

selectedArea.set(areaOptions[0])
areaTypeOptionsMenu = OptionMenu(root, selectedArea, *areaOptions, command=areaSelected)
areaTypeOptionsMenu.config(width=15)


fields = [carrierFrequencyField, antennaheightFieldT,
          antennaheightFieldR, propagationDistanceField, cityTypeOptionsMenu, areaTypeOptionsMenu]
for i in range(6):
    fields[i].grid(row=i + 1, column=2)

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

myButton = Button(root,
                text='Get Path Loss',
                command=getPathLoss,
                fg='white', bg='blue',
                font=labelsfontTypeAndSize
                ).grid(column=1, row=10, padx=20, pady=20)

root.mainloop()
