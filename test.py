from src.HataModel import OkamuraHataModel
# import sys
# from os import path
# sys.path.append('../src')

# from HataModel import OkamuraHataModel


def get_carrier_freq():
    invalid = True
    f_c = 0.0
    while invalid:
        f_c = float(
            input('Enter the value of carrier frequency(150-1500 in MHz): '))
        if (f_c >= 150.0) and (f_c <= 1500.0):
            invalid = False
        else:
            print('Please, enter a valid input. Try again...')
    return f_c


def get_base_station_height():
    invalid = True
    h_t = 0.0
    while invalid:
        h_t = float(
            input('Enter the height of transmitter antenna (30 - 300 in meter): '))
        if (h_t >= 30.0) and (h_t <= 300.0):
            invalid = False
        else:
            print('Please, enter a valid input. Try again...')
    return h_t


def get_mobile_station_height():
    invalid = True
    h_r = 0.0
    while invalid:
        h_r = float(
            input('Enter the height of receiver antenna (1 - 10 in meter): '))
        if (h_r >= 1.0) and (h_r <= 10.0):
            invalid = False
        else:
            print('Please, enter a valid input. Try again...')
    return h_r


def get_link_distance():
    invalid = True
    d = 0.0
    while invalid:
        d = float(input('Enter the are Link distance (1-20 in km): '))
        if (d >= 1.0) and (d <= 20.0):
            invalid = False
        else:
            print('Please, enter a valid input. Try again...')
    return d


def get_city_type():
    invalid = True
    city = 0
    while invalid:
        city = int(input(
            'Enter the integer value of the type of city (1 - Small/Medium, 2-Large): '))
        if (city >= 1) and (city <= 2):
            invalid = False
        else:
            print('Please, enter a valid input. Try again...')
    return city


def get_area_type():
    invalid = True
    area = 0
    while invalid:
        area = int(input(
            'Enter the integer value of the type of area (1 - Urban, 2-Sub urban, 3-Open area): '))
        if (area >= 1) and (area <= 3):
            invalid = False

        else:
            print('Please, enter a valid input. Try again...')
    return area


restart = True
while restart:
    f_c = get_carrier_freq()
    h_t = get_base_station_height()
    h_r = get_mobile_station_height()
    d = get_link_distance()
    city = get_city_type()
    area = get_area_type()
    okamura_hata_model = OkamuraHataModel(
        carrier_freq=f_c, height_transmitter=h_t, height_receiver=h_r, link_distance=d, city=city, area=area)
    print("Path loss (in dB):", okamura_hata_model.path_loss, 'dB')

    reply = int(input('Do you want to exit (1- yes or 2-no): '))

    if reply == 1:
        restart = False
        print('Exiting...')
    else:

        print('Restarting....\n--------------------------------------------------------')
