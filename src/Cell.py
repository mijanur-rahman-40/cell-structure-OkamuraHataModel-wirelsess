import math


class Cell:
    def __init__(self, totalArea, radiusOfCell, frequencyReuseFactor):
        self.totalArea = totalArea
        # self.cellType = cellType
        self.radiusOfCell = radiusOfCell
        self.frequencyReuseFactor = frequencyReuseFactor
        self.numberOfCells = self.getNumberOfCells()
        self.numberOfChannelsPerCell = self.getNumberOfChannelsPerCell()
        self.totalCapacity = self.getTotalCapacity()
        self.totalNumberOfPossibleConcurrentCall = self.getTotalNumberOfConcurrentCall()

    def getNumberOfCells(self):
        areaOfEachCell = float(1.5 * math.sqrt(3) * math.pow(self.radiusOfCell, 2))
        return math.ceil(self.totalArea/areaOfEachCell)

    def getNumberOfChannelsPerCell(self):
        return 1

    def getTotalCapacity(self):
        return self.numberOfCells * self.numberOfChannelsPerCell

    def getTotalNumberOfConcurrentCall(self):
        return 1
