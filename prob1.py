from src.Cell import Cell

restart = 1
while restart == 1:
    total_area = float(input('Enter the area size to cover(in km): '))
    cell_type = int(input('Enter the integer value of cell type (1 -> Macro-cell or 2->Micro-cell>): '))
    while True:
        radius_of_cell = float(input('Enter the radius of cell(in km): '))
        if cell_type == 1:
            if radius_of_cell < 1 or radius_of_cell > 20:
                print('Please enter the value between 1 and 20')
            else:
                break
        else:
            if radius_of_cell < 0.1 or radius_of_cell > 1:
                print('Please enter the value between 0.1 and 1')
            else:
                break
    freq_reuse_factor = int(input('Enter the reuse factor (1 , 3 , 4, 7, 9, 12, 13, 16 , 19 or 21): '))
    cell = Cell(total_area, radius_of_cell, freq_reuse_factor)
    print('Number of cells required: %d' % cell.number_of_cells)
    print('Number of channel per cell: %d' % cell.number_of_channels_per_cell)
    print('Total channel capacity: %d channels' % cell.total_capacity)
    print('Total number of concurrent call: %d' % cell.total_number_of_possible_concurrent_call)

    restart = int(input('Do you want to restart? (1-> yes, 0-> no): '))
