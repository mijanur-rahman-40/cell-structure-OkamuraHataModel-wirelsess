import math


class OkamuraHataModel:
    def __init__(self, carrierierFrequency, heightTransmitter, heightReceiver, linkDistance, city, area):
        self.carrierierFrequency = carrierierFrequency
        self.heightTransmitter = heightTransmitter
        self.heightReceiver = heightReceiver
        self.linkDistance = linkDistance
        self.city = city
        self.area = area
        self.correctionFactor = 0.0
        self.antennaCorrectionFactor()
        self.pathLoss = 0.0
        self.getPathLoss()
        self.countLossVariance()

    def antennaCorrectionFactor(self):
        if self.city == 1:
            self.correctionFactor = (0.8 + ((1.1 * math.log10(self.carrierierFrequency) - 0.7)
                                            * self.heightReceiver) - (1.56 * math.log10(self.carrierierFrequency)))

        else:
            if (self.carrierierFrequency >= 150) and (self.carrierierFrequency <= 200):
                self.correctionFactor = (8.29 * (math.pow(math.log10(1.54 * self.heightReceiver), 2))) - 1.1
            else:
                self.correctionFactor = (3.2 * (math.pow(math.log10(11.75 * self.heightReceiver), 2))) - 4.97

    def getPathLoss(self):
        self.pathLoss = 69.55 + (26.16 * math.log10(self.carrierierFrequency)) - (13.82 * math.log10(self.heightTransmitter)) - self.correctionFactor + ((44.9 - (6.55 * math.log10(self.heightTransmitter)))
             * math.log10(self.linkDistance))

    def countLossVariance(self):
        differenceLoss = 0.0
        if self.area == 1:
            differenceLoss = 2 * math.pow(math.log10((self.carrierierFrequency / 28)), 2) + 5.4

        elif self.area == 2:
            differenceLoss = 4.78 * math.pow(math.log10(self.carrierierFrequency), 2) - 18.33 * math.log10(self.carrierierFrequency) + 40.94

        self.pathLoss -= differenceLoss
