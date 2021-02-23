import math


class Cell:
    def __init__(self, totalArea, radiusOfCell, frequencyReuseFactor):
        self.totalArea = totalArea
        self.radiusOfCell = radiusOfCell
        self.frequencyReuseFactor = frequencyReuseFactor
        self.numberOfCells = self.getNumberOfCells()
        self.numberOfChannelsPerCell = self.getNumberOfChannelsPerCell()
        self.totalCapacity = self.getTotalCapacity()
        self.totalNumberOfPossibleConcurrentCall = self.getTotalNumberOfConcurrentCall()

    def getNumberOfCells(self):
        areaOfEachCell = 1.5 * math.sqrt(3) * self.radiusOfCell ** 2
        return int((self.totalArea / areaOfEachCell) + .5)

    def getNumberOfChannelsPerCell(self):
        return int((self.numberOfCells / self.frequencyReuseFactor) + .5)

    def getTotalCapacity(self):
        return self.numberOfCells * self.numberOfChannelsPerCell

    def getTotalNumberOfConcurrentCall(self):
        return self.totalCapacity
