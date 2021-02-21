import math


class Cell:
    def __init__(self, total_area, radius_of_cell, frequency_reuse_factor):
        self.total_area = total_area
        # self.cell_type = cell_type
        self.radius_of_cell = radius_of_cell
        self.frequency_reuse_factor = frequency_reuse_factor
        self.number_of_cells = self.get_number_of_cells()
        self.number_of_channels_per_cell = self.get_number_of_channels_per_cell()
        self.total_capacity = self.get_total_capacity()
        self.total_number_of_possible_concurrent_call = self.get_total_number_of_concurrent_call()

    def get_number_of_cells(self):
        area_of_each_cell = float(1.5 * math.sqrt(3)*math.pow(self.radius_of_cell, 2))
        return math.ceil(self.total_area/area_of_each_cell)

    def get_number_of_channels_per_cell(self):
        return 1

    def get_total_capacity(self):
        return self.number_of_cells * self.number_of_channels_per_cell

    def get_total_number_of_concurrent_call(self):
        return 1
