def number_of_cells_required(area_size,cell_type, cell_radious):

    hexa_area = 1.5 * math.sqrt(3) * cell_radious ** 2
    exact_number_of_cells_required = area_size / hexa_area
    number_of_cells_required = int(exact_number_of_cells_required + .5)

    # print("Cell type: ", cell_type)
    # print("Hexa_area: ", hexa_area)
    # print("Exact cell required: " , exact_number_of_cells_required)
    return number_of_cells_required

def number_of_channels_per_cell(traffic_channel, reuse_factor):
    exact_number_of_channels_per_cell = traffic_channel/reuse_factor
    number_of_channels_per_cell = int(exact_number_of_channels_per_cell + .5)
    # print("Exact number of channels per cell: ", exact_number_of_channels_per_cell)
    return number_of_channels_per_cell


def total_channel_capacity(number_of_cells_required,number_of_channels_per_cell):
    return number_of_cells_required*number_of_channels_per_cell