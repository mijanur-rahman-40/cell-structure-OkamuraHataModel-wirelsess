from src.Cell import Cell

restart = 1
while restart == 1:
    totalArea = float(input('Enter the area size to cover(in km): '))
    cellType = int(input('Enter the integer value of cell type (1 -> Macro-cell or 2->Micro-cell>): '))
    while True:
        radiusOfCell = float(input('Enter the radius of cell(in km): '))
        if cellType == 1:
            if radiusOfCell < 1 or radiusOfCell > 20:
                print('Please enter the value between 1 and 20')
            else:
                break
        else:
            if radiusOfCell < 0.1 or radiusOfCell > 1:
                print('Please enter the value between 0.1 and 1')
            else:
                break
    freqReuseFactor = int(input('Enter the reuse factor (1 , 3 , 4, 7, 9, 12, 13, 16 , 19 or 21): '))
    cell = Cell(totalArea, radiusOfCell, freqReuseFactor)
    print('Number of cells required: %d' % cell.numberOfCells)
    print('Number of channel per cell: %d' % cell.numberOfChannelsPerCell)
    print('Total channel capacity: %d channels' % cell.totalCapacity)
    print('Total number of concurrent call: %d' % cell.totalNumberOfPossibleConcurrentCall)

    restart = int(input('Do you want to restart? (1-> yes, 0-> no): '))
