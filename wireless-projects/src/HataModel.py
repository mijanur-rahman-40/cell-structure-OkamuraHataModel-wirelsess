import math


class OkamuraHataModel:
    def __init__(self, carrier_freq, height_transmitter, height_receiver, link_distance, city, area):
        self.carrier_frq = carrier_freq
        self.height_transmitter = height_transmitter
        self.height_receiver = height_receiver
        self.link_distance = link_distance
        self.city = city
        self.area = area
        self.corr_factor = 0.0
        self.antenna_corr_factor()
        self.path_loss = 0.0
        self.get_path_loss()
        self.count_loss_variance()

    def antenna_corr_factor(self):
        if self.city == 1:
            self.corr_factor = (0.8 + ((1.1 * math.log10(self.carrier_frq) - 0.7)
                                       * self.height_receiver) - (1.56 * math.log10(self.carrier_frq)))

        else:
            if (self.carrier_frq >= 150) and (self.carrier_frq <= 200):
                self.corr_factor = (
                    8.29 * (math.pow(math.log10(1.54 * self.height_receiver), 2))) - 1.1
            else:
                self.corr_factor = (
                    3.2 * (math.pow(math.log10(11.75 * self.height_receiver), 2))) - 4.97

    def get_path_loss(self):
        self.path_loss = 69.55 + (26.16 * math.log10(self.carrier_frq)) - (13.82 * math.log10(self.height_transmitter)) - \
            self.corr_factor + \
            ((44.9 - (6.55 * math.log10(self.height_transmitter)))
             * math.log10(self.link_distance))

    def count_loss_variance(self):
        diff_loss = 0.0
        if self.area == 2:
            diff_loss = 2 * \
                math.pow(math.log10((self.carrier_frq/28)), 2) + 5.4
        elif self.area == 3:
            diff_loss = 4.78 * \
                math.pow(math.log10(self.carrier_frq), 2) - 18.33 * \
                math.log10(self.carrier_frq) + 40.94

        self.path_loss -= diff_loss
