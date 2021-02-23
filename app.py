from Tkinter import *
import ttk
from src.HataModel import OkamuraHataModel
from src.Cell import Cell

# import sys
# from os import path
# sys.path.append('../src')
# intiate tkinter

root = Tk()
root.title('Okumara/Hata model and cell structure')

# custom style
style = ttk.Style()
style.configure('TEntry', foreground='green')
style.theme_create( "yummy", parent="alt", settings={
        "TNotebook": {"configure": {"tabmargins": [0, 5, 5, 0] } },
        "TNotebook.Tab": {
            "configure": {"padding": [5, 5], "background": 'chocolate', "foreground":"white" },
            "map": {"background": [("selected", 'blueviolet')],
                          "expand": [("selected", [1, 1, 1, 0])] } } } )

style.theme_use("yummy")

notebook = ttk.Notebook(root)

def centerWindow(width, height=200):
    # get screen width and height
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screenHeight / 2) + (-100)
    y = (screenHeight / 2) - (height / 2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))

centerWindow(750, 630)

frame1 = Frame(notebook, width=700, height=600, bg='blueviolet')
frame2 = Frame(notebook, width=700, height=600, bg='chocolate')

notebook.pack(expand=1, fill="both")


notebook.add(frame1, text='Cell structure')
notebook.add(frame2, text='Okumara/Hata model')

# font size and style
headingfontTypeAndSize = ('Helvetica', 20)
labelsfontTypeAndSize = ('Times new Roman', 14)
textFiledFont = ('Times new Roman', 15, 'bold')
outputTextFont = ('Times new Roman', 14, 'bold')

# create  label
def createLabel(frame, background, text, font):
  return Label(frame, bg=background, text=text, font=font, foreground='white')

# create input field
def createEntry(frame, textvariable):
   return ttk.Entry(frame, width=16, textvariable=textvariable, justify=CENTER, font=textFiledFont) 
   
# --------------------- Frame1/Cell structure --------------------

# all input fields variables
totalArea = StringVar()
frequencyReuseFactor = StringVar()
radiusOfCell = StringVar()
selectedCellType = StringVar()
trafficChannel = StringVar()
cellType1 = 'NB(Macro-cell): Radius of each cell(value: 1 to 20)km.'
cellType2 = 'NB(Micro-cell): Radius of each cell(value: .1 to 1)km.'
cellTypeValueInfo = StringVar(value=cellType1)

# label texts
frame1Labels = [
    'Enter the all specified values',
    'Area size to cover (in km)',
    'Radius of each cell (in km)',
    'Total traffic channels',
    'Frequency reuse facto(1,3,4,7,9,12,13,16,19,21..',
    'Select the cell type',
]

# all labels
for i in range(len(frame1Labels)):
    if i == 0:
        createLabel(frame1, 'blueviolet', frame1Labels[i], headingfontTypeAndSize).grid(row=i, column=1, sticky='W', padx=20, pady=15)
    else:
        createLabel(frame1, 'blueviolet', frame1Labels[i], labelsfontTypeAndSize).grid(row=i, column=1, sticky='W', padx=20, pady=10) 

# all input fields
totalAreaFiled = createEntry(frame1, totalArea)
totalAreaFiled.focus_force()
radiusOfCellFiled = createEntry(frame1, radiusOfCell)
radiusOfCellFiled.focus_force()
trafficChannelFiled = createEntry(frame1, trafficChannel)
trafficChannelFiled.focus_force()
frequencyReuseField = createEntry(frame1, frequencyReuseFactor)
frequencyReuseField.focus_force()

# Option menu of type of area
cellTypeOptions = ['Macro-cell', 'Micro-cell']

# info text
Label(frame1,
    bg='blueviolet',
    text=cellType1, font=labelsfontTypeAndSize, foreground='yellow').grid(row=8, column=1, padx=20, pady=15)

def cellTypeSelected(event):
    # info text
    Label(frame1, bg='blueviolet', text=cellType1 if selectedCellType.get() == 'Macro-cell' else cellType2, font=labelsfontTypeAndSize, foreground='yellow').grid(row=8, column=1, padx=20, pady=15)
   

selectedCellType.set(cellTypeOptions[0])
cellTypeOptionsMenu = OptionMenu(frame1, selectedCellType, *cellTypeOptions, command=cellTypeSelected)
cellTypeOptionsMenu.config(width=15)

# all input fields
fields = [totalAreaFiled, radiusOfCellFiled, trafficChannelFiled, frequencyReuseField, cellTypeOptionsMenu]
for i in range(5):
    fields[i].grid(row=i + 1, column=2)

def getAllValues():
    cell = Cell(
        totalArea = int(totalArea.get()),
        radiusOfCell = float(radiusOfCell.get()),
        trafficChannel = int(trafficChannel.get()),
        frequencyReuseFactor = int(frequencyReuseFactor.get())
    )

    Label(frame1, bg='blueviolet', text='Outputs', font=headingfontTypeAndSize, foreground='white').grid(row=11, column=1, padx=20)
    # show all output
    Label(frame1, bg='blueviolet', text='Number of cells required : ' + str(cell.numberOfCells), font=outputTextFont, foreground='white').grid(row=12, column=1, padx=20, pady=2)
    Label(frame1, bg='blueviolet', text='Number of channels per cell : ' + str(cell.numberOfChannelsPerCell), font=outputTextFont, foreground='white').grid(row=13, column=1, padx=20, pady=2)
    Label(frame1, bg='blueviolet', text='Total channel capacity : ' + str(cell.totalCapacity), font=outputTextFont, foreground='white').grid(row=14, column=1, padx=20, pady=2)
    Label(frame1, bg='blueviolet',text='Total number of possible concurrent call : ' + str(cell.totalNumberOfPossibleConcurrentCall), font=outputTextFont, foreground='white').grid(row=15, column=1, padx=20, pady=2)

Button(frame1,
            text='Get all Outputs',
            command=getAllValues,
            fg='white', bg='chocolate',
            font=labelsfontTypeAndSize
            ).grid(column=1, row=10, padx=20, pady=10)
            

# --------------------- Frame2/Okumara/Hata model --------------------

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
frame2Labels = [
    'Enter the all specified values',
    'Value of carrier frequency(150-1500 in MHz)',
    'Height of transmitter antenna(30 - 300 in meter)',
    'Height of receiver antenna (1 - 10 in meter)',
    'Propagation distance between antennas (1 - 20 in km)',
    'Select the type of city',
    'Select the type of area'
]

# all labels
for i in range(len(frame2Labels)):
    if i == 0:
        createLabel(frame2, 'chocolate', frame2Labels[i], headingfontTypeAndSize).grid(row=i, column=1, sticky='W', padx=20, pady=15)
    else:
        createLabel(frame2, 'chocolate', frame2Labels[i], labelsfontTypeAndSize).grid(row=i, column=1, sticky='W', padx=20, pady=10)  

# all input fields
carrierFrequencyField = createEntry(frame2, carrierFrequency)
carrierFrequencyField.focus_force()
antennaheightFieldT = createEntry(frame2, antennaheightT)
antennaheightFieldT.focus_force()
antennaheightFieldR = createEntry(frame2, antennaheightR)
antennaheightFieldR.focus_force()
propagationDistanceField = createEntry(frame2, propagationDistance)
propagationDistanceField.focus_force()

# Option menu of type of city
cityOptions = ['Small/Medium', 'Large']

def citySelected(event):
    selectedCityValue.set(1 if selectedCity.get() == 'Small/Medium' else 2)

selectedCity.set(cityOptions[0])
cityTypeOptionsMenu = OptionMenu(frame2, selectedCity, *cityOptions, command=citySelected)
cityTypeOptionsMenu.config(width=15)

# Option menu of type of area
areaOptions = ['Urban/Suburban', 'Open area']

def areaSelected(event):
    selectedAreaValue.set(1 if selectedArea.get() == 'Urban/Suburban' else 2)

selectedArea.set(areaOptions[0])
areaTypeOptionsMenu = OptionMenu(frame2, selectedArea, *areaOptions, command=areaSelected)
areaTypeOptionsMenu.config(width=15)


fields = [carrierFrequencyField, antennaheightFieldT,
          antennaheightFieldR, propagationDistanceField, cityTypeOptionsMenu, areaTypeOptionsMenu]

for i in range(6):
    fields[i].grid(row=i + 1, column=2)

def getPathLoss():
    okamuraHataModel = OkamuraHataModel(
        carrierierFrequency = int(carrierFrequency.get()),
        heightTransmitter = int(antennaheightT.get()),
        heightReceiver = int(antennaheightR.get()),
        linkDistance = int(propagationDistance.get()),
        city = selectedCityValue.get(),
        area = selectedAreaValue.get()
    )
    Label(frame2, bg='chocolate', text='Outputs', font=headingfontTypeAndSize, foreground='white').grid(row=11, column=1, padx=20)
    Label(frame2,
            text="Path loss (in dB) : " +
            str(okamuraHataModel.pathLoss) + 'dB',
            font=textFiledFont,
            bg='chocolate',
            foreground="white").grid(column=1, row=13, padx=20, pady=20)

Button(frame2,
            text='Get Path Loss',
            command=getPathLoss,
            fg='white', bg='blueviolet',
            font=labelsfontTypeAndSize
            ).grid(column=1, row=10, padx=20, pady=10)



root.mainloop()
